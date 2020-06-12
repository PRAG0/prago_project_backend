from account import models
from rest_framework import viewsets, permissions, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers


class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.UserAccounts.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = serializers.UserAccountSerializer