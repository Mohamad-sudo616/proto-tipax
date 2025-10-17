# tracking/urls.py
from django.urls import path
from . import views

app_name = 'tracking'

urlpatterns = [
    path('', views.track_package, name='track'),
]
