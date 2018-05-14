from HoldApp.forms import ReportForm, HForm, DFormD, DFormF
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from HoldApp.models import DModel, DModelF, DModelD


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
        data_form = HForm(request.POST)

        if report_form.is_valid() and data_form.is_valid():
            report = report_form.save()
            data = data_form.save(commit=False)

            data.report = report
            data.save()

            return redirect('report_list')

    else:
        report_form = ReportForm()
        data_form = HForm()

    return render(request, "contributor/new_report.html", {'report_form': report_form, 'data_form': data_form, })


@user_passes_test(is_contributor)
def new_Dreport(request):
    """Display the New Report form.

    This view combines the Report model and the corresponding data model. This needs to be made into an abstract class
    that can be implemented by ths specific views of different case types.
    """

    # TODO: make this an abstract class to handle every type of report
    if request.method == "POST":
        report_form = ReportForm(request.POST)
        dval_form = DFormD(request.POST)
        fval_form = DFormF(request.POST)

        if report_form.is_valid() and dval_form.is_valid() and fval_form.is_valid():
            report = report_form.save()
            # dval1 = dval_form.save(commit=False)
            # fval1 = fval_form.save(commit=False)

            fval, fcreated = DModelF.objects.get_or_create(**fval_form.cleaned_data)
            dval, dcreated = DModelD.objects.get_or_create(**dval_form.cleaned_data)

            DModel.objects.create(dval=dval, fval=fval, report=report)

            return redirect('report_list')

    else:
        report_form = ReportForm()
        dval_form = DFormD()
        fval_form = DFormF()

    return render(request, "contributor/new_Genreport.html", {'report_form': report_form, 'dval_form': dval_form,
                                                              'fval_form': fval_form})
