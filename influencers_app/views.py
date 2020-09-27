from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.db.models import Sum, Avg, Count
from django.db.models.functions import TruncMonth
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
import re
from googleapiclient.discovery import build

from .models import Influencer, Content, InfluencersInformation, \
    VideoInformation, ArtzProductUS, Shipment

from .forms import InfluencerForm, AuthUserForm, VideoInformationForm, \
    ContentForm, InfluencersInformationForm, ShipmentCreateForm


class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = AuthUserForm
    success_url = reverse_lazy('influencers_list')

    def get_success_url(self):
        return self.success_url


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login_page')


class InfluencersNameSearchMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        influencers_name_search = self.request.GET.get(
            'influencers_name_search')
        if influencers_name_search:
            queryset = queryset.filter(name__icontains=influencers_name_search)
        return queryset


class InfluencerView(InfluencersNameSearchMixin, ListView, LoginRequiredMixin):
    model = Influencer
    login_url = 'login_page'
    # paginate_by = settings.PAGE_SIZE

    @property
    def responsibles(self):
        return User.objects.all()

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        total = Influencer.objects.aggregate(Count('id'))
        context['responsibles'] = self.responsibles
        context['total'] = total['id__count']
        return context


class InfluencerCreateView(CreateView):
    model = Influencer
    form_class = InfluencerForm
    template_name = "influencer_create.html"
    queryset = Influencer.objects.all()

    def get_success_url(self):
        return reverse('influencers_list')

    def form_valid(self, form):
        new_influencer = form.save(commit=False)
        new_influencer_name = new_influencer.name
        new_influencer.save()
        if Influencer.objects.get(name=new_influencer_name):
            InfluencersInformation.objects.get_or_create(
                channel_name_id=new_influencer.id)
        return super().form_valid(form)


class InfluencerUpdateView(UpdateView):
    model = Influencer
    form_class = InfluencerForm
    template_name = "influencer_update.html"

    def get_success_url(self):
        return reverse('influencers_list')


class InfluencersInformationView(LoginRequiredMixin, ListView):
    # TODO:сделать правильный порядок статусов
    login_url = 'login_page'
    template_name = "influencersinformation_list.html"

    def get_template_name(self):
        templates = super().get_template_names()
        if self.kwargs.get('responsible'):
            templates = ["influencersinformation_list.html"]
        return templates

    def get_queryset(self):
        details = InfluencersInformation.objects.select_related(
            'channel_name').order_by('progress')
        influencers_name_search = self.request.GET.get(
            'influencers_name_search')
        if influencers_name_search:
            details = details.filter(
                channel_name__name__icontains=influencers_name_search)
        responsible = self.request.GET.get('responsible')
        if responsible:
            details = details.filter(channel_name__responsible=responsible)
        return details

    def get_context_data(self, object_list=None, **kwargs):
        details = self.get_queryset
        users = User.objects.all()
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['details'] = details
        context['users'] = users
        return context


class InfluencersInformationUpdateView(UpdateView):
    model = InfluencersInformation
    form_class = InfluencersInformationForm
    template_name = 'influencersinformation_update.html'

    def get_success_url(self):
        return reverse('details')


class ContentView(LoginRequiredMixin, ListView):
    model = Content
    login_url = 'login_page'

    def get_template_name(self):
        templates = super().get_template_names()
        if self.kwargs.get('influencer'):
            templates = ["content_list.html"]
        return templates

    def get_queryset(self):
        videos = Content.objects.select_related('channel_name').order_by(
            'date_of_publication')
        influencer = self.request.GET.get('influencer')
        if influencer:
            videos = videos.filter(channel_name__name=influencer)
        return videos

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        videos = self.get_queryset
        video_data_dict = Content.objects.select_related(
            'channel_name').aggregate(
            Sum('number_of_views'), Sum('number_of_comments'),
            Sum('number_of_likes'), Sum('number_of_dislikes'),
            Avg('number_of_views'))
        influencer = self.request.GET.get('influencer')
        context['videos'] = videos
        context['sum_views'] = video_data_dict.get('number_of_views__sum')
        context['sum_comments'] = video_data_dict.get(
            'number_of_comments__sum')
        context['sum_likes'] = video_data_dict.get('number_of_likes__sum')
        context['sum_dislikes'] = video_data_dict.get(
            'number_of_dislikes__sum')
        context['avg'] = video_data_dict.get(
            'number_of_views__avg')
        if influencer:
            filtered_video_data_dict = Content.objects.filter(
                channel_name__name=influencer).select_related(
                'channel_name').aggregate(
                Sum('number_of_views'), Sum('number_of_comments'),
                Sum('number_of_likes'), Sum('number_of_dislikes'),
                Avg('number_of_views'))
            context['sum_views'] = filtered_video_data_dict.get(
                'number_of_views__sum')
            context['sum_comments'] = filtered_video_data_dict.get(
                'number_of_comments__sum')
            context['sum_likes'] = filtered_video_data_dict.get(
                'number_of_likes__sum')
            context['sum_dislikes'] = filtered_video_data_dict.get(
                'number_of_dislikes__sum')
            context['avg'] = filtered_video_data_dict.get(
                'number_of_views__avg')
        return context


class ContentCreateView(CreateView):
    model = Content
    form_class = ContentForm
    template_name = "content_create.html"
    queryset = Content.objects.all()

    def get_success_url(self):
        return reverse('content')

    def form_valid(self, form):

        """If the form is valid, save the associated model."""
        new_video = form.save(commit=False)
        video_url = new_video.video_url
        print(len(video_url))
        if len(video_url) > 11:
            video_url = re.sub(r'https://www\.youtube\.com/watch\?v=', '',
                               video_url)
        print(video_url)
        api_key = settings.API_KEY
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.videos().list(
            part="statistics, snippet",
            id=video_url
        )
        response = request.execute()
        print(response)
        channelTitle = response['items'][0]['snippet']['channelTitle']
        channelId = response['items'][0]['snippet']['channelId']
        new_video.channel_name = Influencer.objects.get_or_create(
            name=channelTitle, channels_url=channelId)[0]
        new_video.video_name = response['items'][0]['snippet']['title']
        new_video.date_of_publication = response['items'][0]['snippet'][
                                            'publishedAt'][0:10]
        new_video.number_of_views = response['items'][0]['statistics'][
            'viewCount']
        new_video.number_of_likes = response['items'][0]['statistics'][
            'likeCount']
        new_video.number_of_dislikes = response['items'][0]['statistics'][
            'dislikeCount']
        new_video.number_of_comments = response['items'][0]['statistics'][
            'commentCount']
        new_video.save()

        return super().form_valid(form)


class ChartView(LoginRequiredMixin, TemplateView):
    model = Content
    template_name = 'influencers_app/chart.html'
    login_url = 'login_page'

    def get_context_data(self, **kwargs):
        video_information_by_month = Content.objects.annotate(
            month=TruncMonth('date_of_publication')).values('month')
        video_count = video_information_by_month.annotate(
            count_of_videos=Count('video_name'),
            sum_of_views=Sum('number_of_views'),
            sum_of_comments=Sum('number_of_comments'))
        for item in video_count:
            item['month'] = item.get('month').strftime('%Y %b')
        context = super().get_context_data(**kwargs)
        context['qs'] = Content.objects.select_related('channel_name')

        if self.kwargs['pk'] == 1:
            for item in video_count:
                item['total'] = item.get('count_of_videos')
            context['title'] = 'Count of videos'
        elif self.kwargs['pk'] == 2:
            for item in video_count:
                item['total'] = item.get('sum_of_views')
            context['title'] = 'Sum of video views'
        elif self.kwargs['pk'] == 3:
            for item in video_count:
                item['total'] = item.get('sum_of_comments')
            context['title'] = 'Sum of comments'
        context['video_count_month'] = video_count
        return context


class VideoInformationView(ListView):
    model = VideoInformation
    form_class = VideoInformationForm
    template_name = "videoinformation_list.html"
    queryset = VideoInformation.objects.all()


# class VideoInformationCreateView(CreateView):
"""Это было тестовое вью, удалить потом"""
#     model = VideoInformation
#     form_class = VideoInformationForm
#     template_name = "videoinformation_create.html"
#     queryset = VideoInformation.objects.all()
#
#     def get_success_url(self):
#         return reverse('video')
#
#
#     def form_valid(self, form):
#
#         """If the form is valid, save the associated model."""
#         new_video = form.save(commit=False)
#         video_id = new_video.video_id
#         print(len(video_id))
#         if len(video_id) > 11:
#             video_id = re.sub(r'https://www\.youtube\.com/watch\?v=', '',
#             video_id)
#
#         print(video_id)
#         api_key = settings.API_KEY
#         youtube = build('youtube', 'v3', developerKey=api_key)
#         request = youtube.videos().list(
#             part="statistics, snippet",
#             id=video_id
#         )
#         response = request.execute()
#         print(response)
#         title = response['items'][0]['snippet']['title']
#         publishedAt = response['items'][0]['snippet']['publishedAt']
#         channelId = response['items'][0]['snippet']['channelId']
#         channelTitle = response['items'][0]['snippet']['channelTitle']
#         print(title)
#         print(publishedAt)
#         print(channelId)
#         print( channelTitle)
#         new_video.views_count = response['items'][0]['statistics'][
#         'viewCount']
#         new_video.likes_count = response['items'][0]['statistics'][
#         'likeCount']
#         new_video.dislikes_count = response['items'][0]['statistics'][
#         'dislikeCount']
#         new_video.comments_count = response['items'][0]['statistics'][
#         'commentCount']
#         new_video.save()
#         return super().form_valid(form)


class ArtzProductUSView(ListView):
    model = ArtzProductUS
    template_name = "artzproductus_list.html"
    queryset = ArtzProductUS.objects.all()


class ShipmentView(ListView):
    model = Shipment
    template_name = "shipment_list.html"
    queryset = Shipment.objects.all().order_by('-shipment_status')


class ShipmentCreateView(CreateView):
    model = Shipment
    form_class = ShipmentCreateForm
    template_name = 'shipment_create.html'

    def get_success_url(self):
        return reverse('shipment')


class ShipmentUpdateView(UpdateView):
    model = Shipment
    form_class = ShipmentCreateForm
    template_name = 'shipment_update.html'

    def get_success_url(self):
        return reverse('shipment')
