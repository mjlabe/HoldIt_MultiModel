from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Report(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now())
    mod_date = models.DateTimeField(blank=True, null=True)


class GroupRequest(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    GROUP_CHOICES = (
        ('U', 'User'),
        ('C', 'Contributor')
    )
    group = models.CharField(max_length=1, choices=GROUP_CHOICES, default='U')
