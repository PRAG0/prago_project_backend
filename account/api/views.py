from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from account import models
from . import serializers
from . import permissions


class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.UserAccounts.objects.all()
    serializer_class = serializers.UserAccountSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnAccount,)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = serializers.LoginSerializer
    query_set = models.UserAccounts.objects.all()

    def create(self, request):
        """유효한 필드 값인지 확인 후 Token 생성"""

        return ObtainAuthToken().post(request)
