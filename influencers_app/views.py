from django.db.models import Sum, Avg, Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import ContextMixin
from django.contrib.auth.models import User

from .models import Influencer, Content, InfluencersInformation
from django.conf import settings

from .forms import InfluencerForm
from time import strftime


class InfluencerView(ContextMixin, View):
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


class InfluencersInformationView(ListView):

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
        print(object_list)
        context['details'] = details
        return context


class ContentView(ListView):

    model = Content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Content.objects.select_related('channel_name').order_by('date_of_publication')
        context['sum_views'] = Content.objects.aggregate(
            Sum('number_of_views')).get('number_of_views__sum')
        context['sum_comments'] = Content.objects.aggregate(
            Sum('number_of_comments')).get('number_of_comments__sum')
        context['sum_likes'] = Content.objects.aggregate(
            Sum('number_of_likes')).get('number_of_likes__sum')
        context['sum_dislikes'] = Content.objects.aggregate(
            Sum('number_of_dislikes')).get('number_of_dislikes__sum')
        context['avg'] = Content.objects.aggregate(Avg('number_of_views')).get('number_of_views__avg')
        return context


class ChartView(TemplateView):
    model = Content
    template_name = 'influencers_app/chart.html'


    def get_context_data(self, **kwargs):
        video_count = Content.objects.annotate(
            month=TruncMonth('date_of_publication')).values('month').annotate(
            total=Count('video_name'))
        for item in video_count:
            item['month'] = item.get('month').strftime('%Y %b')
        print(video_count)
        context = super().get_context_data(**kwargs)
        context['qs'] = Content.objects.select_related('channel_name')
        context['video_count_month'] = video_count
        return context
