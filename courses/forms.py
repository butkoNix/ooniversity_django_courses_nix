from django import forms
from courses.models import Course


class ModelCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name',
            'short_description',
            'description',
            'coach',
            'assistant',
        ]
