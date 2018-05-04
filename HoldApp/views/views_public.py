from HoldApp.forms import ReportForm, DataForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def header(request):
    return render(request, 'header.html')


def footer(request):
    return render(request, 'footer.html')


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
