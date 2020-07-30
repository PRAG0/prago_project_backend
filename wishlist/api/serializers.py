import requests
import json

from rest_framework import serializers
from wishlist import models

from django.http import JsonResponse, HttpResponse


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WishLists
        fields = ('user_id', 'product_name', 'product_price', 'product_image', 'product_site_link', 'product_site_name')

    def list(self, request):
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

    def create(self, validated_data):
        print(validated_data)
        if validated_data:
            dump_data = json.dumps(validated_data, ensure_ascii=False)
            json_data = json.loads(dump_data)

            if models.WishLists.objects.distinct(json_data['product_image']):
                return HttpResponse(status=207)
            else:
                models.WishLists(
                    user_id=json_data['user_id'],
                    product_name=json_data['product_name'],
                    product_price=json_data['product_price'],
                    product_image=json_data['product_image'],
                    product_site_name=json_data['product_site_name'],
                    product_site_link=json_data['product_site_link']
                ).save()
        else:
            return HttpResponse(status=204)

        return HttpResponse(status=200)

    def desrtory(self, request):
        query = models.WishLists.objects.all()

        if request['product_site_name'] in query:
            models.WishLists.delete(product_site_name=request['product_site_name'])
            return HttpResponse(status=200)

        else:
            return HttpResponse(status=204)
