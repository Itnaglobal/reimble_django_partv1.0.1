# Generated by Django 3.2.9 on 2021-11-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_usermodel_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=220, null=True),
        ),
    ]
