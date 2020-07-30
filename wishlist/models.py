from django.db import models


class WishLists(models.Model):
    """찜 목록 모델"""

    user_id = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_price = models.CharField(max_length=255)
    product_image = models.TextField(default="")
    product_site_link = models.TextField()
    product_site_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
