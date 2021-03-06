# Generated by Django 3.2.9 on 2021-11-09 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_usermodel_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='is_new_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='is_user',
            field=models.BooleanField(default=False),
        ),
    ]
