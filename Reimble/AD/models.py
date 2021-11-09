from datetime import datetime

from django.db import models
from Account.models import UserModel, Country
# Create your models here.


class AdCategory(models.Model):
    ad_category_name = models.CharField(max_length=220, default=None)

    def __str__(self):
        return self.ad_category_name


class AdSubcategory(models.Model):
    ad_subcategory_name = models.CharField(max_length=220, default=None)

    def __str__(self):
        return self.ad_subcategory_name


class AD(models.Model):
    CHOICE_IMPRESSION = (
        ("POSITIVE", "POSITIVE"),
        ("OVER POSITIVE", "OVER POSITIVE"),
        ("NEGATIVE", "NEGATIVE"),
        ("VERY POOR", "VERY POOR")
    )
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    ad_title = models.CharField(max_length=220)
    ad_category = models.ForeignKey(AdCategory, on_delete=models.CASCADE)
    ad_subcategory = models.ForeignKey(AdSubcategory, on_delete=models.CASCADE)
    ad_views = models.PositiveIntegerField(default=0)
    ad_impression = models.CharField(max_length=220, choices=CHOICE_IMPRESSION, null=True)
    reach = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.ad_title
