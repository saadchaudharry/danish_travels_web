from django import forms
from .models import Carousel,Client_review,Employer,Employee



class Employer_form(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['company_name', 'full_name', 'email_address', 'phone_number', 'employee_name', 'occupation', 'message']

class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email_address', 'phone_number', 'message']

