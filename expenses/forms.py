from django import forms
from .models import Expense

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'date_of_expense', 'category', 'description', 'amount']
        widgets = {
            'date_of_expense': forms.DateInput(attrs={'type': 'date'}),
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
    
    def save(self,commit=True):
        user= super(SignUpForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user