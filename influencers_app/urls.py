from django.urls import path

from . import views

urlpatterns = [
    path('login', views.UserLoginView.as_view(), name='login_page'),
    path('logout', views.UserLogoutView.as_view(), name='logout_page'),
    path('influencers/', views.InfluencerView.as_view(), name='influencers_list'),
    path('details/', views.InfluencersInformationView.as_view(), name='details'),
    path('content', views.ContentView.as_view(), name='content'),
    path('content/charts/<int:pk>', views.ChartView.as_view(), name='charts'),
]