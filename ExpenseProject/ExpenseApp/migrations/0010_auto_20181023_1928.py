# Generated by Django 2.0.6 on 2018-10-23 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseApp', '0009_remove_transactionmodel_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactionmodel',
            old_name='date_Submitted',
            new_name='date_Submittd',
        ),
        migrations.RemoveField(
            model_name='transactionmodel',
            name='first_name',
        ),
        migrations.AddField(
            model_name='transactionmodel',
            name='expenseFK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ExpenseApp.ExpenseModel'),
        ),
    ]
