# Generated by Django 5.0 on 2023-12-30 05:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
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
                (
                    "video_title",
                    models.CharField(max_length=264, verbose_name="Put a Title"),
                ),
                ("slug", models.SlugField(max_length=264, unique=True)),
                (
                    "video_description",
                    models.TextField(verbose_name="Video description..."),
                ),
                (
                    "video_file",
                    models.FileField(upload_to="videos", verbose_name="Video File"),
                ),
                ("publish_date", models.DateTimeField(auto_now_add=True)),
                ("update_date", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-publish_date"],
            },
        ),
    ]
