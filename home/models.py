from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone
from classes.models import Class


class Post(models.Model):
    title = models.CharField(max_length=255)
    post_files1 = models.FileField(upload_to='images/', null=True, blank=True)
    post_files2 = models.FileField(upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")
        #return reverse("article-detail", args=(str(self.id)))


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.post.title, self.name)