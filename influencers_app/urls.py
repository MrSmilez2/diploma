from django.urls import path

from . import views

urlpatterns = [
    path('influencers/', views.InfluencerView.as_view()),
    path('details/', views.InfluencersInformationView.as_view(), name='details'),
    path('content', views.ContentView.as_view()),
    path('content/charts', views.ChartView.as_view(), name='charts'),
]