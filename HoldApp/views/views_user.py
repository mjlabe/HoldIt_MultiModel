from django.http import HttpResponseRedirect
from HoldApp.models.models import Report
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.views import View
from ..forms import ReportForm
from django.utils.decorators import method_decorator


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


# class ReportDetail(View):
#     form_class = ReportForm
#     initial = {'key': 'value'}
#     template_name = 'user/report_detail.html'
#
#     @method_decorator(user_passes_test(is_user))
#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
#
#     @method_decorator(user_passes_test(is_user))    # TODO: dont do this!!!!
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             return HttpResponseRedirect('/success/')
#
#         return render(request, self.template_name, {'form': form})


