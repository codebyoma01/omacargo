from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('track/', views.track_shipment, name='track'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),

    # Individual service pages
    path('services/air-freight/', views.air_freight, name='air_freight'),
    path('services/sea-freight/', views.sea_freight, name='sea_freight'),
    path('services/road-transport/', views.road_transport, name='road_transport'),
    path('services/warehousing/', views.warehousing, name='warehousing'),
]
