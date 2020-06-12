from rest_framework import routers
from django.urls.conf import path, include
from . import views
#from account.api.views import


router = routers.DefaultRouter()
router.register('account', views.AccountViewSet)


urlpatterns = router.urls
