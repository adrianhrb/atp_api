from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'api_matches'
router = routers.DefaultRouter()
router.register('matches', views.MatchViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('matches/<pk>/winner/', views.MatchWinnerView.as_view(), name='match_winner'),
    path('matches/<pk>/loser/', views.MatchLoserView.as_view(), name='match_loser'),
]
