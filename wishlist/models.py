from django.db import models

from account.models import UserAccounts


class WishLists(models.Model):
    """찜 목록 모델"""

    favor_user_id = models.ForeignKey(UserAccounts, on_delete=models.CASCADE, to_field='user_id', related_name='wishlists', default="")
    product_name = models.CharField(max_length=255)
    product_price = models.CharField(max_length=255)
    product_image = models.TextField(default="")
    product_site_link = models.TextField()
    product_site_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
