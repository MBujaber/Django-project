from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    opening_time = models.DateField()
    closing_time = models.DateField()
    created_at = models.DateTimeField()
