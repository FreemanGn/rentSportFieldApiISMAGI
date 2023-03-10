# Generated by Django 4.1.5 on 2023-01-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_team_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="type",
            name="name",
            field=models.CharField(
                choices=[
                    ("FB", "Football"),
                    ("BB", "Basketball"),
                    ("T", "Tennis"),
                    ("HB", "Handball"),
                    ("N", "Natation"),
                    ("SP", "Skatepark"),
                    ("P", "Patinoire"),
                    ("SG", "Streetgym"),
                    ("VB", "Volleyball"),
                ],
                max_length=5,
                unique=True,
            ),
        ),
    ]
