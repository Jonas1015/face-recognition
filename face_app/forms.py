from django import forms
from .models import *

# Create your forms here
class addStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fname', 'sname', 'lname', 'regno', 'course', 'year', 'phoneNumber', 'image']
        labels = {
            'fname': 'First Name',
            'sname': 'Middle Name',
            'lname': 'Last Name',
            'regno': 'Registration Number',
            'phoneNumber': 'Mobile Phone'
        }

class addCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name']


class updateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fname', 'sname', 'lname', 'regno', 'course', 'year', 'phoneNumber', 'image']
        labels = {
            'fname': 'First Name',
            'sname': 'Middle Name',
            'lname': 'Last Name',
            'regno': 'Registration Number',
            'phoneNumber': 'Mobile Phone'
        }


class updateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name']
