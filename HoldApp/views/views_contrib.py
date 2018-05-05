from HoldApp.forms import ReportForm, DataForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test


def is_contributor(user):
    return user.groups.filter(name='Contributor').exists()


#TODO: use middleware instead of decorators
@user_passes_test(is_contributor)
def new_report(request):
    if request.method == "POST":
        report_form = ReportForm(request.POST)
        data_form = DataForm(request.POST)

        if report_form.is_valid() and data_form.is_valid():
            report = report_form.save()
            data = data_form.save(commit=False)

            data.report = report
            data.save()

            return redirect('report_list')

    else:
        report_form = ReportForm()
        data_form = DataForm()

    return render(request, "contributor/new_report.html", {'report_form': report_form, 'data_form': data_form, })
