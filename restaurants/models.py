from django.db import models
# from django.utils import timezone


# class AutoDateTimeField(models.DateTimeField):
#     def pre_save(self, model_instance, add):
#         return timezone.now()


class Post(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=None)
    opening_time = models.DateField()
    closing_time = models.DateField()
    created_at = models.DateField(auto_now=True)
