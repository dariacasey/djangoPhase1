# Generated by Django 4.2.5 on 2023-09-30 01:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lessons", "0016_studentscore_remove_exerciseset_score_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercise",
            name="student_answer",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
