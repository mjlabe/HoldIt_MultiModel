from django.db import models
from django.utils import timezone


class Data(models.Model):
    report = models.ForeignKey('HoldApp.Report', on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now())
    mod_date = models.DateTimeField(blank=True, null=True)
