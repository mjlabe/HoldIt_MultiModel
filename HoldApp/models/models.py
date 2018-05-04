from django.db import models
from django.utils import timezone


class Report(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now())
    mod_date = models.DateTimeField(blank=True, null=True)


