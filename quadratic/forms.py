from django import forms


class QuadraticForm(forms.Form):

    a = forms.CharField(max_length=10)
    b = forms.CharField(max_length=10)
    c = forms.CharField(max_length=10)
