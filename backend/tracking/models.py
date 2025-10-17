from django.db import models
from django.utils import timezone

class Package(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('in_transit', 'In Transit'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('exception', 'Exception'),
    ]
    tracking_code = models.CharField(max_length=64, unique=True)
    current_status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='created')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tracking_code

class PackageEvent(models.Model):
    package = models.ForeignKey(Package, related_name='events', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=128, blank=True)
    status = models.CharField(max_length=32, choices=Package.STATUS_CHOICES)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-timestamp']
