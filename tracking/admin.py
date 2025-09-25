from django.contrib import admin
from .models import Shipment

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ("tracking_number", "sender", "receiver", "status", "created_at")
    search_fields = ("tracking_number", "sender", "receiver")
    list_filter = ("status", "created_at")

