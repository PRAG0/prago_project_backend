from django.db import models


class SiteInfo(models.Model):
    site_name = models.CharField(max_length=255, null=True)
    prodt_name = models.CharField(max_length=255, null=True, blank=True)
    prodt_price = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)