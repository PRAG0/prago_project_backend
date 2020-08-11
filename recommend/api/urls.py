from rest_framework import routers
from . import views
from django.urls import path


router = routers.DefaultRouter()
router.register('recommend-list', views.RecommendListViewSet)

urlpatterns = router.urls
