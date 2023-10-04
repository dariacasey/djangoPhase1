from django.contrib import admin
from .models import Lesson, Exercise, ExerciseSet, StudentScore

admin.site.register(Lesson)
admin.site.register(Exercise)
admin.site.register(ExerciseSet)
admin.site.register(StudentScore)

