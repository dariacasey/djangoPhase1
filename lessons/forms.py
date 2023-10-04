from django import forms
from .models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['question', 'option_1', 'option_2', 'option_3', 'correct_answer', 'student_answer']
