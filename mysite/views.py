from django.shortcuts import render
from catalog.models import Event, Image
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.urls import reverse


def serialize_image(image):
    return {
        'image': image.image
    }

def get_image_url(image):
    path = image.get_absolute_image_url
    return path


def serialize_place(event):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [event.longitude, event.latitude]
          },
        "properties": {
            "title": event.title,
            "detailsUrl": reverse(place_detail, kwargs={'place_id': event.id})
          }
          }

def show_main(request):
    moscow_events = Event.objects.all()
    geojson = {
        "type": "FeatureCollection",
        "features": [serialize_place(event) for event in moscow_events]
    }
    context = {'geojson': geojson}
    return render(request, 'index.html', context)


def place_detail(request, place_id):
    event = get_object_or_404(Event, id=place_id)
    images = Image.objects.filter(event_name=event.id).order_by('number')
    event_dict = {
        'title': event.title,
        'imgs': [get_image_url(image) for image in images],
        'description_short': event.short_description,
        'description_long': event.long_description,
        'coordinates': {
            'lon': event.longitude,
            'lat': event.latitude}}
    response = JsonResponse(event_dict, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    return response
