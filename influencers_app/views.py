from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import ContextMixin
from django.contrib.auth.models import User
from .models import Influencer, Content


from .forms import InfluencerForm


class InfluencerView(ContextMixin, View):

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
        responsibles = self.responsibles
        form = InfluencerForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'influencers_list.html', {
            "influencers": influencers,
            "responsibles": responsibles
        })

