# Generated by Django 4.2.5 on 2023-09-18 03:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="user_type",
            field=models.CharField(max_length=10),
        ),
    ]
