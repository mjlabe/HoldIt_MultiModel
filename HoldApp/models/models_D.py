from django.db import models
from .models import DateCreateModMixin


class DModel(DateCreateModMixin):
    report = models.ForeignKey('HoldApp.Report', on_delete=models.CASCADE)
    fval = models.ForeignKey('HoldApp.DModelF', on_delete=models.CASCADE)
    dval = models.ForeignKey('HoldApp.DModelD', on_delete=models.CASCADE)


class DModelF(models.Model):
    fval = models.FloatField(max_length=100)


class DModelD(models.Model):
    dval = models.IntegerField()
