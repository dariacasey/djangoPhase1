from django.db import models
from django.contrib.auth.models import User
import uuid


class Class(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='classes')
    class_code = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)

    def __str__(self):
        return self.name
