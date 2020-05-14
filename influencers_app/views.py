from django.db.models import Sum, Avg
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import ContextMixin
from django.contrib.auth.models import User
from .models import Influencer, Content, InfluencersInformation
from django.conf import settings

from .forms import InfluencerForm


class InfluencerView(ContextMixin, View):
    paginate_by = settings.PAGE_SIZE
    @property
    def responsibles(self):
        return User.objects.all()

    def get(self, request):
        influencers = Influencer.objects.all()
        return render(request, 'influencers_list.html', {
            "influencers": influencers,
            "responsibles": responsibles
        })

    def post(self, request, *args, **kwargs):
        influencers = Influencer.objects.all()
        form = InfluencerForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'influencers_list.html', {
            "influencers": influencers,
            "responsibles": responsibles
        })


class InfluencersInformationView(ListView):

    model = InfluencersInformation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['details'] = InfluencersInformation.objects.select_related('channel_name')
        return context


class ContentView(ListView):

    model = Content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Content.objects.select_related('channel_name')
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