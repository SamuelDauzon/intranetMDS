#coding: utf-8
from datetime import datetime
import concurrent.futures

from django.core.management.base import BaseCommand
from django.conf import settings

import requests

from calls.models import UrlSite

class Command(BaseCommand):

    def site_availability(self, urlsite):
        try:
            r = requests.get(urlsite.url)
            r.raise_for_status()
        except Exception as e:
            urlsite.available = False
        else:
            urlsite.available = True
        urlsite.save()

    def handle(self, *args, **options):

        # urlsite = UrlSite(url="https://google.fr").save()
        # UrlSite(url="https://microsoft.fr").save()
        # UrlSite(url="https://amazon.fr").save()
        # UrlSite(url="https://stackoverflow.com").save()
        # UrlSite(url="https://docs.djangoproject.com").save()
        # UrlSite(url="https://github.com").save()
        # UrlSite(url="https://githubijsdjlmk.com").save()

        urlsites = UrlSite.objects.all()
        startTime = datetime.now()

        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            for urlsite in urlsites:
                executor.submit(self.site_availability, urlsite)

        # for urlsite in urlsites:
        #     self.site_availability(urlsite)

        print(datetime.now() - startTime)
