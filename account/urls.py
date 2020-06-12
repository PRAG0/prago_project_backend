from django.contrib import admin
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('signup/', views.),
]