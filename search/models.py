from django.db import models


class SiteInfo(models.Model):
    url = models.URLField()
    site_name = models.CharField(max_length=255, null=True)
    image_tag = models.CharField(max_length=255, null=True, blank=True)
    prodt_price_tag = models.CharField(max_length=255, null=True, blank=True)
    prodt_name_tag = models.CharField(max_length=255, null=True, blank=True)
