import re
from django import forms
from .models import *

# Create your forms here
class addStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fname', 'sname', 'lname', 'regno', 'course', 'year', 'email', 'phoneNumber', 'image']
        labels = {
            'fname': 'First Name',
            'sname': 'Middle Name',
            'lname': 'Last Name',
            'regno': 'Registration Number',
            'phoneNumber': 'Mobile Phone',
        }
        #
        # def clean_phone(self):
        #     phone = self.cleaned_data.get('phoneNumber')
        #     x = re.search("^\+?1?\d{10,15}$", phone)
        #     if x != x:
        #         raise forms.ValidationError("Enter Valid Format!")
        #     return phone
        #
        #
        # def clean_regNo(self):
        #     regNo = self.cleaned_data.get('regno')
        #     y = re.search("^[A-Z]{3}/[A-Z]{3}/\d{2}/\d{5}$", regNo)
        #     if y != y:
        #         raise forms.ValidationError("Enter Valid Format!")
        #     return regNo

class addCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name']


class updateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fname', 'sname', 'lname', 'regno', 'course', 'year','email', 'phoneNumber', 'image']
        labels = {
            'fname': 'First Name',
            'sname': 'Middle Name',
            'lname': 'Last Name',
            'regno': 'Registration Number',
            'phoneNumber': 'Mobile Phone',
        }


class updateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name']



class TestVideoForm(forms.ModelForm):
    class Meta:
        model = TestVideo
        fields = ['video']
