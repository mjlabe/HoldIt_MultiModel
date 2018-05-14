from django.db import models
from django.utils import timezone
from .models import DateCreateModMixin


class HModel(DateCreateModMixin):
    report = models.ForeignKey('HoldApp.Report', on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
