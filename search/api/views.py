import json
import requests

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import permissions

from search import models

from bs4 import BeautifulSoup


@method_decorator(csrf_exempt, name='dispatch')
class SearchListView(View):
    def post(self, request):
        url_list = models.SiteInfo.objects.filter().values_list('url')
        site_name_list = models.SiteInfo.objects.filter().values_list('site_name')
        prodt_name_tag_list = models.SiteInfo.objects.filter().values_list('prodt_name_tag')
        prodt_price_tag_list = models.SiteInfo.objects.filter().values_list('prodt_price_tag')
        image_tag_list = models.SiteInfo.objects.filter().values_list('image_tag')

        prodt_name = []
        prodt_price = []
        image = []

        data = json.loads(str(request.body))

        for i in range(len(models.SiteInfo.objects.count())):

            req = requests.get(f'{url_list[i]}{data["query"]}')
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            prodt_name.append(soup.select(
                prodt_name_tag_list[i]
            )[0].text)

            prodt_price.append(soup.select(
                prodt_price_tag_list[i]
            )[0].text)

            # image.append(soup.select(
            #     models.SiteInfo.image_tag[i]
            # ))
            print(prodt_price, prodt_name)

        return





