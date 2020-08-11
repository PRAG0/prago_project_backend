from rest_framework import viewsets

from recommend.models import RecommendProducts
from recommend.api import serializers


class RecommendListViewSet(viewsets.ModelViewSet):
    queryset = RecommendProducts.objects.all()
    serializer_class = serializers.RecommendListSerializer
