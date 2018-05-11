from HoldApp.models.models import Report
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test


def is_user(user):
    return user.groups.filter(name='User').exists() | user.groups.filter(name='Contributor').exists() | \
           user.groups.filter(name='Worker').exists() | user.groups.filter(name='Admin').exists()


# TODO: limit the number of reports requested
@user_passes_test(is_user)
def report_list(request):
    """Display a list of Reports sorted by newest to oldest"""

    reports = Report.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'user/report_list.html', {'reports': reports})


@user_passes_test(is_user)
def report_detail(request, pk):
    """Display the detailed view for a Report"""

    report = get_object_or_404(Report, pk=pk)
    return render(request, 'user/report_detail.html', {'report': report})
