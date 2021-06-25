from django import forms
from .models import *


class InsertStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('date_of_creation', 'status')


class InsertCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class InsertStudentCourse(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = '__all__'
