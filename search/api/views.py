import requests
import json

from search import models
from .crawl import crawlilng

from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import permissions

from bs4 import BeautifulSoup


@method_decorator(csrf_exempt, name='dispatch')
class SearchListView(View):
    def post(self, request):

        models.SiteInfo.objects.all().delete()

        data = json.loads(request.body)
        products_name, products_price, products_image, products_site_name, products_site_link = crawlilng(data['query'])

        models.SiteInfo(
            product_name=products_name,
            product_price=products_price,
            product_image=products_image,
            product_site_link=products_site_link,
            product_site_name=products_name,
        ).save()

        return HttpResponse(status=200)

    def get(self, request):
        return JsonResponse({'search list': list(models.SiteInfo.objects.values())}, status=200)
