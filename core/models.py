from django.db import models

class Cargo(models.Model):
    tracking_id = models.CharField(max_length=20, unique=True)
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(
        max_length=50,
        choices=[
            ("pending", "Pending"),
            ("in_transit", "In Transit"),
            ("delivered", "Delivered"),
        ],
        default="pending",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tracking_id} - {self.status}"

