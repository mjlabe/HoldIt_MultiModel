from HoldApp.forms import ReportForm, DataForm, DForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test


def is_contributor(user):
    """Verify User is a Contributor"""

    return user.groups.filter(name='Contributor').exists() | user.groups.filter(name='Worker').exists() | \
           user.groups.filter(name='Admin').exists()


# TODO: use middleware instead of decorators
@user_passes_test(is_contributor)
def new_report(request):
    """Display the New Report form.

    This view combines the Report model and the corresponding data model. This needs to be made into an abstract class
    that can be implemented by ths specific views of different case types.
    """

    # TODO: make this an abstract class to handle every type of report
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


@user_passes_test(is_contributor)
def new_dform(request):
    if request.method == "POST":
        report_form = DForm(request.POST)

        if report_form.is_valid():
            report_form.save()

            return redirect('report_list')

    else:
        report_form = DForm()

    return render(request, "contributor/new_dreport.html", {'report_form': report_form,})