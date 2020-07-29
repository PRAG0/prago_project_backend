from django.db import models


class SiteInfo(models.Model):
    index = models.AutoField(primary_key=True)
    product_name = models.TextField(max_length=255, default="")
    product_price = models.IntegerField()
    product_image = models.TextField(default="")
    product_site_name = models.TextField(max_length=255, default="")
    product_site_link = models.TextField(default="")

    class Meta:
        ordering = ['product_price']
