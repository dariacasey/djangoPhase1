# Generated by Django 4.2.5 on 2023-09-24 14:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lessons", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lesson",
            name="class_field",
        ),
        migrations.RemoveField(
            model_name="lesson",
            name="order",
        ),
    ]
