# Generated by Django 4.2.5 on 2023-10-02 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_remove_profile_user_type_profile_is_student_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="last_logout_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
