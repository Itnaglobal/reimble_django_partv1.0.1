# Generated by Django 3.2.9 on 2021-11-03 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_usermodel_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
