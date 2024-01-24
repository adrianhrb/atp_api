from django.urls import path
from . import views

urlpatterns = [
    path('ai/', views.form_ai, name='form_ai')
]
