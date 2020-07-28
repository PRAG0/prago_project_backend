from django.db import models


class SiteInfo(models.Model):
    product_name = models.CharField(max_length=255, default="")
    product_price = models.CharField(max_length=255, default="")
    product_image = models.TextField(default="")
    product_site_name = models.CharField(max_length=255, default="")
    product_site_link = models.TextField(default="")

    class Meta:
        ordering = ['product_price'*1]
