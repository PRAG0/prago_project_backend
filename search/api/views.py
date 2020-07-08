import json
import requests
from django.http import JsonResponse

from django.shortcuts import render
from django.views import View

from search import models

from bs4 import BeautifulSoup


class SearchListView(View):
    pass
    def post(self, request):
        url_list = models.SiteInfo.objects.filter().values_list('url')
        site_name_list = models.SiteInfo.objects.filter().values_list('site_name')
        prodt_name_tag_list = models.SiteInfo.objects.filter().values_list('prodt_name_tag')
        prodt_price_tag_list = models.SiteInfo.objects.filter().values_list('prodt_price_tag')
        image_tag_list = models.SiteInfo.objects.filter().values_list('image_tag')

        prodt_name = []
        prodt_price = []
        image = []

        data = json.loads(request.body)

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

        return JsonResponse({prodt_name, prodt_price}, status=200)





