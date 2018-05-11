from django.db import models
from .models import Report


class DModel(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    dVal = models.IntegerField(max_length=50)
    fVal = models.FloatField(max_length=20)


class DReport(DModel, Report, models.Model):
    class Meta:
        abstract = True

    pass
