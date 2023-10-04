from django.contrib.auth.models import User
from django.db import models
from classes.models import Class


# This model is created so the user type (Teacher or Student) is stored in the admin database
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    # for post indicator
    last_logout_time = models.DateTimeField(null=True, blank=True)
    # to show correct posts on home page
    class_field = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.user)
