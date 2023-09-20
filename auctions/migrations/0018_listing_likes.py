# Generated by Django 4.2.1 on 2023-09-19 14:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0017_listing_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="listings", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]