# Generated by Django 3.0.5 on 2020-07-24 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0030_auto_20200724_1812"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vehicle",
            old_name="charging_Rate",
            new_name="charging_rate",
        ),
    ]
