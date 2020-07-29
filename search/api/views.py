import requests
import json

from search import models
from .crawl import crawlilng

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class SearchListView(View):
    def get(self, request):
        products_name = []
        products_price = []
        products_image = []
        products_site_name = []
        products_site_link = []
        models.SiteInfo.objects.all().delete()

        query = request.GET.get('query')
        products_name, products_price, products_image, products_site_name, products_site_link = crawlilng(query)

        for i in range(len(products_price)):
            match = products_price[i] \
                .replace('최저', '') \
                .replace('원', '') \
                .replace(',', '')

            products_price[i] = match

        for i in range(len(products_name)):
            models.SiteInfo(
                index=i+1,
                product_name=products_name[i],
                product_price=products_price[i],
                product_image=products_image[i],
                product_site_link=products_site_link[i],
                product_site_name=products_site_name[i],
            ).save()

        return JsonResponse(list(models.SiteInfo.objects.values()), safe=False, status=200)
