from django.urls import path

from . import views

app_name = 'matches'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('match/', views.MatchView.as_view(), name='match'),
    path('<int:pk>/', views.MatchDetailView.as_view(), name='matchdetail'),
    path('post/', views.MatchCreateView.as_view(), name='matchpost'),
]