from email.policy import default
from django.db import models
# from django.utils import timezone


# class AutoDateTimeField(models.DateTimeField):
#     def pre_save(self, model_instance, add):
#         return timezone.now()


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default="")
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.TimeField(auto_now_add=True)
