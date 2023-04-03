from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")


class Tag(models.Model):
    name = models.CharField(max_length=63)
