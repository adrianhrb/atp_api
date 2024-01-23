from django.urls import path

from .views import load_data

urlpatterns = [path('kaggle/', load_data, name='load')]
