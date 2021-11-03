# Generated by Django 3.2.9 on 2021-11-03 12:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0004_usermodel_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_category_name', models.CharField(default=None, max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='AdSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_subcategory_name', models.CharField(default=None, max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='AD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('ad_title', models.CharField(max_length=220)),
                ('ad_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AD.adcategory')),
                ('ad_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AD.adsubcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.usermodel')),
            ],
        ),
    ]
