# Generated by Django 4.2.6 on 2024-06-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserDetailes",
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
                ("name", models.TextField()),
                ("dep", models.TextField()),
                ("phone", models.IntegerField()),
                ("blood", models.TextField()),
            ],
        ),
    ]
