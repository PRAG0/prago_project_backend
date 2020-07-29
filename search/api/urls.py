from rest_framework import routers
from . import views
from django.urls import path


router = routers.DefaultRouter()
router.register(r'wishlist', views.WishListView.as_view, basename='wishList')

urlpatterns = [
    path('search/', views.SearchListView.as_view()),
]
