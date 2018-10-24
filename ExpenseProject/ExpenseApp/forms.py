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


class DepositForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['deposits']


class WithdrawForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['withdraws']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['deposits','withdraws']