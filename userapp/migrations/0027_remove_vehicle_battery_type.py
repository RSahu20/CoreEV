# Generated by Django 3.0.5 on 2020-07-16 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0026_auto_20200716_1244"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicle",
            name="battery_type",
        ),
    ]
