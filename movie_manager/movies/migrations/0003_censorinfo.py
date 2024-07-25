# Generated by Django 5.0.6 on 2024-06-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_alter_movieinfo_director_alter_movieinfo_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="CensorInfo",
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
                ("rating", models.CharField(max_length=10, null=True)),
                ("authority", models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
