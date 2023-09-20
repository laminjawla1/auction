# Generated by Django 4.2.1 on 2023-09-18 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watch_listed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='watch_listed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watch_listed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='WatchList',
        ),
    ]