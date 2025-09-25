from django.db import models

class Shipment(models.Model):
    tracking_number = models.CharField(max_length=100, unique=True)
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    status = models.CharField(max_length=100, default="In Transit")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tracking_number} - {self.status}"

