from django.db import models
from django.contrib.auth.models import User
from classes.models import Class


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    lesson_files = models.FileField(upload_to='lesson_files/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    lesson_class = models.ManyToManyField(Class, related_name='lessons')

    def __str__(self):
        return self.title


class Exercise(models.Model):
    question = models.TextField()
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    correct_answer = models.PositiveIntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')])
    student_answer = models.PositiveIntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')], default=1)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class ExerciseSet(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    exercises = models.ManyToManyField('Exercise', related_name='exercise_sets')


class StudentScore(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_set = models.ForeignKey(ExerciseSet, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Score for {self.student.username} in ExerciseSet {self.exercise_set.id}"

