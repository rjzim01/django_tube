# Generated by Django 5.0 on 2023-12-30 08:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("App_Video", "0003_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="video_thumbnail",
            field=models.ImageField(
                default=None,
                null=True,
                upload_to="video_thumbnail",
                verbose_name="Image",
            ),
        ),
    ]
