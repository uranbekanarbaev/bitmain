from django.core.management.base import BaseCommand
from main.models import Product
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

class Command(BaseCommand):
    help = 'Scrape products from the website and import them into the database'

    def handle(self, *args, **kwargs):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

        # Set up the Chrome driver
        service = Service('C:/chromedriver-win64/chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            # Open the URL
            driver.get('https://shop.bitmain.com')

            # Wait for the page to fully load
            time.sleep(5)

            # Get the page source
            html = driver.page_source

            # Use BeautifulSoup to parse the page source
            soup = BeautifulSoup(html, 'html.parser')

            # Find all 'a' tags
            a_tags = soup.find_all('a')
            data = {}
            for item in a_tags:
                href = item.get('href')  # Get the href attribute

                # Find the span with class 'name' inside the <a> tag
                name_tag = item.find('span', class_='name')
                
                if name_tag and href:
                    data[name_tag.text] = href

            # Clean up old data
            Product.objects.all().delete()

            # Import the scraped data into the database
            for name, url in data.items():
                product, created = Product.objects.get_or_create(name=name, link=f'https://shop.bitmain.com{url}')
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added product: {name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Product already exists: {name}'))

            self.stdout.write(self.style.SUCCESS(f'Successfully imported data from the scraped content'))

        finally:
            # Close the browser
            driver.quit()
