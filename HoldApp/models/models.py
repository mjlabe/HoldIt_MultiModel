from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class DateCreateModMixin(models.Model):
    class Meta:
        abstract = True

    created_date = models.DateTimeField(default=timezone.now)
    mod_date = models.DateTimeField(blank=True, null=True)


class Report(DateCreateModMixin):
    """This model common to every type of device. It includes common things like, title, summary, device type, etc."""
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=100000, blank=True, null=True)


class GroupRequest(DateCreateModMixin):
    """This model associates a "Group Request" (access privilege request) to the User model during signup. The user is
    not added to the group (and therefore has no access privileges) until an Administrator assigns them to that Group."""

    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    GROUP_CHOICES = (
        ('U', 'User'),
        ('C', 'Contributor')
    )
    group = models.CharField(max_length=1, choices=GROUP_CHOICES, default='U')
