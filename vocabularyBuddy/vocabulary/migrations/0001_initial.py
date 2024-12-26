# Generated by Django 4.2.17 on 2024-12-26 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Word",
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
                ("word", models.CharField(max_length=50)),
                ("pronunciation", models.CharField(blank=True, max_length=100)),
                ("meaning", models.TextField(blank=True)),
                ("example", models.TextField(blank=True)),
                ("proficiency", models.FloatField(default=0.0)),
            ],
        ),
    ]
