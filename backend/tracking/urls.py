
from django.urls import path
from .views import TrackPackageView

urlpatterns = [
    path('', TrackPackageView.as_view(), name='track_package'),
]
