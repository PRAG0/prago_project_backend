import requests
import json

from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import serializers
from rest_framework.decorators import action

from wishlist import models
from account.models import UserAccounts

from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WishLists
        fields = (
            'id',
            'favor_user_id',
            'product_name',
            'product_price',
            'product_image',
            'product_site_link',
            'product_site_name')

    def get(self, request):
        favor_user_id = request.GET.get['favor_user_id']
        query = models.WishLists.objects.get(user_id=favor_user_id)
        if query:
            return JsonResponse(
                {
                    "id": query.id,
                    "product_name": query.product_name,
                    "product_price": query.product_price,
                    "product_image": query.product_image,
                    "product_site_name": query.product_site_name,
                    "product_site_link": query.product_site_link,
                }, status=200)
        else:
            return HttpResponse(204)

    def post(self, validated_data):
        if validated_data:
            if models.WishLists.objects.filter(
                    favor_user_id=validated_data['favor_user_id'], product_image=validated_data['product_image']).exists():
                return HttpResponse(status=207)
            else:
                models.WishLists(
                    favor_user_id=validated_data['favor_user_id'],
                    product_name=validated_data['product_name'],
                    product_price=validated_data['product_price'],
                    product_image=validated_data['product_image'],
                    product_site_name=validated_data['product_site_name'],
                    product_site_link=validated_data['product_site_link']
                ).save()
        else:
            return HttpResponse(status=204)

        return HttpResponse(status=200)

    def update(self, instance, validated_data):
        query = models.WishLists.objects.all()

        if validated_data['id'] in query:
            instance = models.WishLists.objects.filter(
                product_site_name=validated_data['product_site_name'],
                favor_user_id=validated_data['favor_user_id']
            ).delete()
            return super().update(instance, validated_data)
        else:
            return HttpResponse(status=204)
