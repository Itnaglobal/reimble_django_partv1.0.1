from django.db import models
from Account.models import *


class GroupRole(models.Model):
    ROLE_CHOICES = (
        ("ADMIN", "ADMIN"),
        ("EDITOR", "EDITOR"),
        ("NORMAL USER", "NORMAL USER")
    )
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    role = models.CharField(max_length=220, choices=ROLE_CHOICES)

    class Meta:
        ordering = ['-user']

    def __str__(self):
        return str(self.role)


class GroupModel(models.Model):
    slug = models.SlugField(unique=True)
    group_name = models.CharField(max_length=220)
    group_profile_picture = models.ImageField(upload_to="images/")
    user = models.ManyToManyField(UserModel)
    group_closed = models.BooleanField(default=False)

    def __str__(self):
        return '%d: %s' % (self.id, self.group_name)


class GroupPost(models.Model):
    title = models.CharField(max_length=320)
    content = models.TextField()
    attachments = models.FileField(upload_to="files/")
    group = models.ForeignKey(GroupModel, on_delete=models.DO_NOTHING, related_name="groups")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.title)


