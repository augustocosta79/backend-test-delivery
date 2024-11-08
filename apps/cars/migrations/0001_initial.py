# Generated by Django 4.2.14 on 2024-11-07 13:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=60, verbose_name="name")),
                ("year", models.PositiveIntegerField(verbose_name="year")),
                ("description", models.TextField(verbose_name="description")),
                ("sold", models.BooleanField(default=False, verbose_name="sold")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
            ],
        ),
    ]
