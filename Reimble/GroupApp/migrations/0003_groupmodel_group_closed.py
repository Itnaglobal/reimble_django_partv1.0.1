# Generated by Django 3.2.9 on 2021-11-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupApp', '0002_rename_context_grouppost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmodel',
            name='group_closed',
            field=models.BooleanField(default=False),
        ),
    ]
