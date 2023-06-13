# Generated by Django 4.1.4 on 2023-06-05 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_remove_shop_creator_remove_shop_timestamp_shop_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reviews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("review", models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(name="RouteComment",),
        migrations.AddField(
            model_name="shop",
            name="average_rating",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="shop",
            name="instagram",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="shop",
            name="website",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="shopupvote",
            name="upvote",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="saved_shops",
            field=models.ManyToManyField(to="api.shop"),
        ),
        migrations.AddField(
            model_name="reviews",
            name="shop",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="api.shop",
            ),
        ),
        migrations.AddField(
            model_name="reviews",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews_made",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
