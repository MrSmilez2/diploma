from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Sum, Avg, Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.base import ContextMixin
from django.contrib.auth.models import User

from .models import Influencer, Content, InfluencersInformation
from django.conf import settings

from .forms import InfluencerForm, AuthUserForm
from time import strftime


class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = AuthUserForm
    success_url = reverse_lazy('influencers_list')

    def get_success_url(self):
        return self.success_url


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login_page')


class InfluencerView(LoginRequiredMixin, ContextMixin, View):
    login_url = 'login_page'
    paginate_by = settings.PAGE_SIZE

    @property
    def responsibles(self):
        return User.objects.all()

    def get(self, request):
        influencers = Influencer.objects.all()
        responsibles = self.responsibles
        return render(request, 'influencers_list.html', {
            "influencers": influencers,
            "responsibles": responsibles
        })

    def post(self, request, *args, **kwargs):
        influencers = Influencer.objects.all()
        form = InfluencerForm(request.POST)
        responsibles = self.responsibles
        if form.is_valid():
            form.save()
        return render(request, 'influencers_list.html', {
            "influencers": influencers,
            "responsibles": responsibles,
        })


class InfluencersInformationView(LoginRequiredMixin, ListView):
    login_url = 'login_page'
    # model = InfluencersInformation
    template_name = "influencersinformation_list.html"

    def get_template_name(self):
        templates = super().get_template_names()
        if self.kwargs.get('responsible'):
            templates = ["influencersinformation_list.html"]
        return templates

    def get_queryset(self):
        details = InfluencersInformation.objects.select_related('channel_name')
        responsible = self.request.GET.get('responsible')
        if responsible:
            details = details.filter(channel_name__responsible=responsible)
        return details

    def get_context_data(self, object_list=None, **kwargs):
        details = self.get_queryset
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['details'] = details
        return context


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
            influencer = influencer[1:-1]
            videos = videos.filter(channel_name__name=influencer)
        return videos

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        videos = self.get_queryset
        influencer = self.request.GET.get('influencer')
        context['videos'] = videos
        context['sum_views'] = Content.objects.select_related(
            'channel_name').aggregate(
            Sum('number_of_views')).get('number_of_views__sum')
        context['sum_comments'] = Content.objects.aggregate(
            Sum('number_of_comments')).get('number_of_comments__sum')
        context['sum_likes'] = Content.objects.aggregate(
            Sum('number_of_likes')).get('number_of_likes__sum')
        context['sum_dislikes'] = Content.objects.aggregate(
            Sum('number_of_dislikes')).get('number_of_dislikes__sum')
        context['avg'] = Content.objects.aggregate(Avg('number_of_views')).get(
            'number_of_views__avg')
        if influencer:
            context['sum_views'] = Content.objects.filter(
                channel_name__name=influencer[1:-1]).select_related(
                'channel_name').aggregate(
                Sum('number_of_views')).get('number_of_views__sum')
            context['sum_comments'] = Content.objects.filter(
                channel_name__name=influencer[1:-1]).aggregate(
                Sum('number_of_comments')).get('number_of_comments__sum')
            context['sum_likes'] = Content.objects.filter(
                channel_name__name=influencer[1:-1]).aggregate(
                Sum('number_of_likes')).get('number_of_likes__sum')
            context['sum_dislikes'] = Content.objects.filter(
                channel_name__name=influencer[1:-1]).aggregate(
                Sum('number_of_dislikes')).get('number_of_dislikes__sum')
            context['avg'] = Content.objects.filter(
                channel_name__name=influencer[1:-1]).aggregate(
                Avg('number_of_views')).get('number_of_views__avg')
        return context


class ChartView(LoginRequiredMixin, TemplateView):
    model = Content
    template_name = 'influencers_app/chart.html'
    login_url = 'login_page'

    def get_context_data(self, **kwargs):
        video_count = Content.objects.annotate(
            month=TruncMonth('date_of_publication')).values('month').annotate(
            total=Count('video_name'))
        sum_of_views = Content.objects.annotate(
            month=TruncMonth('date_of_publication')).values('month').annotate(
            total=Sum('number_of_views'))
        sum_of_comments = Content.objects.annotate(
            month=TruncMonth('date_of_publication')).values('month').annotate(
            total=Sum('number_of_comments'))
        for item in video_count:
            item['month'] = item.get('month').strftime('%Y %b')
        print(video_count)
        context = super().get_context_data(**kwargs)
        context['qs'] = Content.objects.select_related('channel_name')

        if self.kwargs['pk'] == 1:
            context['title'] = 'Count of videos'
            context['video_count_month'] = video_count
        elif self.kwargs['pk'] == 2:
            context['title'] = 'Sum of video views'
            context['video_count_month'] = sum_of_views
        elif self.kwargs['pk'] == 3:
            context['title'] = 'Sum of comments'
            context['video_count_month'] = sum_of_comments
        return context
