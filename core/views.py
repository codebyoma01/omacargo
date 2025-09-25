from django.shortcuts import render
from tracking.models import Shipment

def home(request):
    return render(request, 'home.html')

def track_shipment(request):
    query = request.GET.get("tracking_number")
    shipment = None
    if query:
        try:
            shipment = Shipment.objects.get(tracking_number=query)
        except Shipment.DoesNotExist:
            shipment = None
    return render(request, 'track.html', {"shipment": shipment, "query": query})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

# Individual service pages
def air_freight(request):
    return render(request, 'services/air_freight.html')

def sea_freight(request):
    return render(request, 'services/sea_freight.html')

def road_transport(request):
    return render(request, 'services/road_transport.html')

def warehousing(request):
    return render(request, 'services/warehousing.html')
