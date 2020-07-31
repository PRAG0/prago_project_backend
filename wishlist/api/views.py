from wishlist import models
from . import serializers

from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets


class WishListViewSet(viewsets.ModelViewSet):
    queryset = models.WishLists.objects.all()
    serializer_class = serializers.WishListSerializer
    # permission_classes = (permissions.UpdateOwnAccount,)

    # def create(self, request, *args, **kwargs):
    #
    #     return HttpResponse(self.queryset.all())
