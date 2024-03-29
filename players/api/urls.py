from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'api_players'
router = routers.DefaultRouter()
router.register('players', views.PlayerViewSet)

urlpatterns = [path('', include(router.urls))]
