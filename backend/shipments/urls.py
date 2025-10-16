from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_package, name='send_package'),
]
