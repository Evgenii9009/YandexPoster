from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from django.urls import reverse


from places.models import Event


def serialize_place(event):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [event.longitude, event.latitude]
          },
        "properties": {
            "title": event.title,
            "detailsUrl": reverse(place_detail, kwargs={
                "place_id": event.id
                })
          }
          }


def show_main(request):
    map_events = Event.objects.all()
    geojson = {
        "type": "FeatureCollection",
        "features": [serialize_place(event) for event in map_events]
    }
    context = {"geojson": geojson}
    return render(request, "index.html", context)


def place_detail(request, place_id):
    event = get_object_or_404(Event.objects.prefetch_related('images'), id=place_id)
    images = event.images.all().order_by("number")
    event_parameters = {
        "title": event.title,
        "imgs": [image.get_absolute_image_url for image in images],
        "description_short": event.short_description,
        "description_long": event.long_description,
        "coordinates": {
            "lon": event.longitude,
            "lat": event.latitude
            }}
    response = JsonResponse(event_parameters, safe=False,
                            json_dumps_params={
                                "ensure_ascii": False,
                                "indent": 4
                                })
    return response
