# Generated by Django 4.2.5 on 2023-09-30 02:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lessons", "0017_exercise_student_answer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exercise",
            name="student_answer",
            field=models.PositiveIntegerField(
                choices=[(1, "Option 1"), (2, "Option 2"), (3, "Option 3")], default=1
            ),
        ),
    ]