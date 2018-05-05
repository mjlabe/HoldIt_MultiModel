from HoldApp.models.models import Report
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


# TODO: limit the number of reports requested
@login_required
def report_list(request):
    reports = Report.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'user/report_list.html', {'reports': reports})


@login_required
def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'user/report_detail.html', {'report': report})
