from django.db import models


class SiteURL(models.Model):
    URL = models.CharField(max_length=255)
