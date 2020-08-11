from rest_framework import serializers

from recommend.models import RecommendProducts

from django.http import JsonResponse, HttpResponse


class RecommendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendProducts
        fields = '__all__'

    def get(self, request):
        if RecommendProducts.objects.all().exists():
            recommend_data = RecommendProducts.objects.all()
            return JsonResponse(list(recommend_data.values()), status=200, safe=False)
        else:
            return HttpResponse(status=204)

    def post(self):
        pass

    def update(self, instance, validated_data):
        pass
