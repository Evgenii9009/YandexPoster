from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.exceptions import MultipleObjectsReturned


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
        try:
            event, _ = Event.objects.get_or_create(title=place["title"],
                                                   defaults={'long_description': "",
                                                             'short_description': "",
                                                             'latitude': 55,
                                                             'longitude': 37, })
        except MultipleObjectsReturned:
            print('Событие уже есть в базе данных!')
        try:
            for image_number, image_url in enumerate(place["imgs"]):
                response = requests.get(image_url)
                response.raise_for_status()
                name = image_url.split("/")[-1]
                image = ContentFile(response.content)
                try:
                    new_image, created = Image.objects.get_or_create(image,
                                                                     number=image_number,
                                                                     event_name=event)
                    if created:
                        new_image.image.save(name,
                                             image,
                                             save=True)
                except MultipleObjectsReturned:
                    print(f'Изображение {image_number} уже есть в базе данных!')
        except ConnectionError:
            pass
        except requests.exceptions.HTTPError:
            pass
