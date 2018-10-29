from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class ExpenseModel(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    date_Submitted = models.DateTimeField(default=datetime.now)
    current_balance = models.FloatField(default=0,)
    emergency_fund = models.FloatField(default=0,)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)

    #
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.first_name


class UserSetup(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=257)
    email = models.EmailField(max_length=200)
    nameFK = models.ForeignKey(ExpenseModel, on_delete=models.SET_NULL, null=True, blank=True,)

    def __str__(self):
        return self.first_name


class TransactionModel(models.Model):
    deposits = models.FloatField(default=0, null=True, blank=True,)
    withdraws = models.FloatField(default=0, null=True, blank=True,)
    reason = models.CharField(max_length=50, null=True, blank=True)
    date_Submittd = models.DateTimeField(default=datetime.now)
    expenseFK = models.ForeignKey(ExpenseModel, on_delete=models.SET_NULL, null=True, blank=True,)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.date_Submittd)