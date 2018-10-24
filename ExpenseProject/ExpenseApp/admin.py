from django.contrib import admin
from .models import ExpenseModel, UserSetup, TransactionModel


admin.site.register(ExpenseModel)
admin.site.register(UserSetup)
admin.site.register(TransactionModel)