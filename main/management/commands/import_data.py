import json
from django.core.management.base import BaseCommand
from main.models import Product  # Replace 'your_app' with your actual app name

class Command(BaseCommand):
    help = 'Import products from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file to read data from')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        Product.objects.all().delete()

        with open(json_file, 'r') as file:
            data = json.load(file)
            for name, url in data.items():
                product, created = Product.objects.get_or_create(name=name, link=f'https://shop.bitmain.com{url}')
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added product: {name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Product already exists: {name}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully imported data from "{json_file}"'))
