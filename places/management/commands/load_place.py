from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile


import requests


from places.models import Event, Image


class Command(BaseCommand):
    help = "load place info from json file"

    def add_arguments(self, parser):
        parser.add_argument("url", type=str, help="Url of the needed file")

    def handle(self, **kwargs):
        file_url = kwargs["url"]
        response = requests.get(file_url)
        response.raise_for_status()
        place = response.json()
        event, _ = Event.objects.get_or_create(title=place["title"],
                                               short_description=place["description_short"],
                                               long_description=place["description_long"],
                                               latitude=place["coordinates"]["lat"],
                                               longitude=place["coordinates"]["lng"])
        for image_number, image_url in enumerate(place["imgs"]):
            response = requests.get(image_url)
            response.raise_for_status()
            name = image_url.split("/")[-1]
            new_image, _ = Image.objects.get_or_create(image=ImageFile(response.content),
                                                       number=image_number,
                                                       event_name=event)
            new_image.image.save(name,
                                 ContentFile(response.content),
                                 save=True)
