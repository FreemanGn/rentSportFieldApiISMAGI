# Generated by Django 4.1.5 on 2023-01-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_terrain_image_terrain_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="type",
            name="image",
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
