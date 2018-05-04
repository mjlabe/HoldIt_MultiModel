from HoldApp.forms import ReportForm, DataForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def header(request):
    return render(request, 'header.html')


def footer(request):
    return render(request, 'footer.html')


def new_report(request):
    if request.method == "POST":
        report_form = ReportForm(request.POST)
        data_form = DataForm(request.POST)

        if report_form.is_valid() and data_form.is_valid():
            report = report_form.save()
            data = data_form.save(commit=False)

            data.report = report
            data.save()

            return redirect('index')

    else:
        report_form = ReportForm()
        data_form = DataForm()

    context = {
        'report_form': report_form,
        'data_form': data_form,
    }

    return render(request, "new_report.html", {'report_form': report_form, 'data_form': data_form, })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # uncomment the code below to make the new account inactive until an admin approves
            # user = form.save(commit=False)
            # user.is_active = False
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration\signup.html', {'form': form})
