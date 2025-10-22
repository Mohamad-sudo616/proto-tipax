from django.urls import path
from .views import SendPackageView

urlpatterns = [
    path('send/', SendPackageView.as_view(), name='send_package'),
]
