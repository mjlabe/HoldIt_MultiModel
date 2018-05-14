from django import forms
from HoldApp.models import Report, HModel, GroupRequest, DModel, DModelF, DModelD
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ReportForm(forms.ModelForm):
    # title = forms.CharField(label='Title')
    class Meta:
        model = Report
        fields = ('title', 'summary', )


class HForm(forms.ModelForm):
    # data = forms.CharField(label='Data')
    class Meta:
        model = HModel
        fields = ('data', )


class DFormF(forms.ModelForm):
    class Meta:
        model = DModelF
        fields = ('fval', )


class DFormD(forms.ModelForm):
    class Meta:
        model = DModelD
        fields = ('dval', )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class GroupChoiceForm(forms.ModelForm):
    class Meta:
        model = GroupRequest
        fields = ('group', )
