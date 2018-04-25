from django import forms
from django.core.validators import RegexValidator


class QuadraticForm(forms.Form):
    a = forms.CharField(
        label='коэффициент a:',
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[-]?[0-9]*$',
                message='коэффициент не целое число',
                code='invalid_value'
            ),
            RegexValidator(
                regex='^[^0]*$',
                message='коэффициент при первом слагаемом уравнения не может быть равным нулю',
                code='invalid_value'
            ),
        ]
    )
    b = forms.CharField(
        label='коэффициент b:',
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[-]?[0-9]*$',
                message='коэффициент не целое число',
                code='invalid_value'
            )
        ]
    )
    c = forms.CharField(
        label='коэффициент c:',
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[-]?[0-9]*$',
                message='коэффициент не целое число',
                code='invalid_value'
            )
        ]
    )
