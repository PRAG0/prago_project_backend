from rest_framework import routers
from django.urls.conf import path, include
from . import views


router = routers.DefaultRouter()
router.register('account', views.AccountViewSet)
router.register('login', views.LoginViewSet, basename='login')

urlpatterns = router.urls