from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from account import models
from . import serializers
from . import permissions


class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.UserAccounts.objects.all()
    serializer_class = serializers.UserAccountSerializer