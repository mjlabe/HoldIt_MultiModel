from django import forms
from HoldApp.models import Report, Data


class ReportForm(forms.ModelForm):
    # title = forms.CharField(label='Title')
    class Meta:
        model = Report
        fields = ('title', )


class DataForm(forms.ModelForm):
    # data = forms.CharField(label='Data')
    class Meta:
        model = Data
        fields = ('data', )
