from wishlist import models
from . import serializers

from rest_framework import viewsets
from account.api import permissions


class WishListViewSet(viewsets.ModelViewSet):
    queryset = models.WishLists.objects.all()
    serializer_class = serializers.WishListSerializer
    # permission_classes = (permissions.UpdateOwnAccount,)
