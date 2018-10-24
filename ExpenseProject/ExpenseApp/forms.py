from django import forms
from .models import ExpenseModel, UserSetup, TransactionModel


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseModel
        fields = ['first_name','last_name', 'current_balance', 'emergency_fund', 'expenses', 'username' ]

        # order_field = {'first_name','last_name', 'deposits', 'withdraws', 'current_balance', 'emergency_fund', 'expenses'}


class UserForm(forms.ModelForm):
    class Meta:
        model = UserSetup
        fields = ['first_name','email', 'password',]
        widgets = {
            'password': forms.PasswordInput(),
        }


class TransactionForm(forms.Form):
    deposits = forms.DecimalField(default=0,max_digits=25, decimal_places=2)
    withdraws = forms.DecimalField(default=0,max_digits=25, decimal_places=2)
