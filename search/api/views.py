import json
import requests

from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import permissions

from search import models

from bs4 import BeautifulSoup


@method_decorator(csrf_exempt, name='dispatch')
class SearchListView(View):
    url = ['https://www.coupang.com/np/search?component=&q=', 'https://browse.gmarket.co.kr/search?keyword=']
    prodt_name_tag = ['#\31 083851471 > a > dl > dd > div > div.name', 'div:nth-child(3) > div:nth-child(1) > div > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item']
    prodt_price_tag = ['', 'div:nth-child(3) > div:nth-child(1) > div > div.box__information > div.box__information-major > div.box__item-price > div > strong']
    image_tag = ['', 'div:nth-child(3) > div:nth-child(1) > div > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item']

    def post(self, request):
        models.SiteInfo.objects.all().delete()
        data = json.loads(request.body)


        data = json.loads(request.body, encoding="UTF-8")





