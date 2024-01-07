# Generated by Django 3.0.5 on 2020-04-25 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0013_auto_20200416_2342"),
    ]

    operations = [
        migrations.CreateModel(
            name="Support",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=20, verbose_name="Title")),
                (
                    "description",
                    models.TextField(
                        max_length=200, verbose_name="Describe issue you are facing"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="support_requests",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
