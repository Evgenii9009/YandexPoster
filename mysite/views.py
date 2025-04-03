from django.shortcuts import render
from catalog.models import Event, Image

def serialize_image(image):
    return {
        'image': image.image
    }


#def serialize_event(event):
#    images = Image.objects.filter(event_name=event.id).order_by('number')
#    return {
#        'title': event.title,
#        'short_descriprion': event.short_description,
#        'long_description': event.long_description,
#        'lon': event.longitude,
#        'lat': event.latitude,
#        'images': [serialize_image(image) for image in images]
#    }

def serialize_place(event):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [event.longitude, event.latitude]
          },
        "properties": {
            "title": event.title,
            "placeId": event.place_id,
            "detailsUrl": ""
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
