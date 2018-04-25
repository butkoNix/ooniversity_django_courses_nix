from django import forms
from students.models import Student


class ModelStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'surname',
            'date_of_birth',
            'email',
            'phone',
            'address',
            'skype',
            'courses',
        ]
