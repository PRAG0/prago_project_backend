from django.db import models


class RecommendProducts(models.Model):
    index = models.AutoField(primary_key=True)
    recommend_product_name = models.TextField(max_length=255, default="")
    recommend_product_price = models.IntegerField()
    recommend_product_image = models.TextField(default="")
    recommend_product_site_name = models.TextField(max_length=255, default="")
    recommend_product_site_link = models.TextField(default="")

    class Meta:
        ordering = ['recommend_product_price']
