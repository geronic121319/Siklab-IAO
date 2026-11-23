from django.db import models


class Incident(models.Model):
    description = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    severity = models.CharField(max_length=32, default="unknown")
    reporter_id = models.CharField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
