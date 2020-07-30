from rest_framework import routers
from django.urls import path

from . import views


router = routers.DefaultRouter()
router.register('wishlist', views.WishListViewSet)

urlpatterns = router.urls