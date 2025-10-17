# shipments/models.py
from django.db import models
from django.conf import settings
import uuid

class Package(models.Model):
    SHIP_TYPE_CHOICES = [
        ('درون‌شهری', 'درون‌شهری'),
        ('بین‌شهری', 'بین‌شهری'),
    ]

    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ship_type = models.CharField(max_length=20, choices=SHIP_TYPE_CHOICES, default='بین‌شهری')
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    from_address = models.TextField()
    to_address = models.TextField()
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2)
    send_date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # ✅ NEW FIELD
    tracking_code = models.CharField(max_length=12, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.tracking_code:
            self.tracking_code = f"PKG-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sender.username} → {self.to_location} ({self.tracking_code})"
