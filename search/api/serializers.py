import requests
import json

from rest_framework import serializers
from account import models
from search import models
from .crawl import crawlilng

from django.http import JsonResponse, HttpResponse


class WishListSerializer(serializers.Serializer):
    def get(self, request):
        user_id = request.GET.get['user_id']
        query = models.WishLists.objects.get(user_id=user_id)
        if query:
            return JsonResponse(
                {
                    "product_name": query.product_name,
                    "product_price": query.product_price,
                    "product_image": query.product_image,
                    "product_site_name": query.product_site_name,
                    "product_site_link": query.product_site_link,
                }, status=200)
        else:
            return HttpResponse(204)

    def post(self, request):
        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            models.WishLists(
                user_id=request['user_id'],
                product_name=request['product_name'],
                product_price=request['product_price'],
                product_image=request['product_image'],
                product_site_name=request['product_site_name'],
                product_site_link=request['product_site_link']
            ).save()
        else:
            models.WishLists(
                user_id=request.POST['user_id'],
                product_name=request.POST['product_name'],
                product_price=request.POST['product_price'],
                product_image=request.POST['product_image'],
                product_site_name=request.POST['product_site_name'],
                product_site_link=request.POST['product_site_link']
            ).save()

        return HttpResponse(status=200)

    def delete(self, request):
        query = models.WishLists.objects.all()

        if request['product_site_name'] in query:
            models.WishLists.delete(product_site_name=request['product_site_name'])
            return HttpResponse(status=200)

        else:
            return HttpResponse(status=204)