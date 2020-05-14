from django.urls import path

from . import views

urlpatterns = [
    path('influencers', views.InfluencerView.as_view()),
    path('details', views.InfluencersInformationView.as_view()),
    path('content', views.ContentView.as_view()),
]