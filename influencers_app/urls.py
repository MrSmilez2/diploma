from django.urls import path

from . import views

urlpatterns = [
    path('influencers', views.InfluencerView.as_view()),
]