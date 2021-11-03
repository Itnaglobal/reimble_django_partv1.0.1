from django.db import models
from datetime import datetime

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=220)
    country_logo = models.ImageField(upload_to="imgaes/")

    def __str__(self):
        return self.country_name


class Professions(models.Model):
    title = models.CharField(max_length=220)

    def __str__(self):
        return self.title


class UserModel(models.Model):
    CHOICE_SEX = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        ("OTHERS", "OTHERS")
    )
    created_at = models.DateTimeField(default=datetime.now)
    first_name = models.CharField(max_length=220)
    last_name = models.CharField(max_length=220)
    username = models.CharField(max_length=220, unique=True)
    profile_image = models.ImageField(upload_to="images/")
    cover_photo = models.ImageField(upload_to="images/")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    professions = models.ForeignKey(Professions, on_delete=models.CASCADE)
    sex = models.CharField(max_length=220, choices=CHOICE_SEX, null=True)
    password = models.CharField(max_length=220, null=True)

    def __str__(self):
        return self.username


