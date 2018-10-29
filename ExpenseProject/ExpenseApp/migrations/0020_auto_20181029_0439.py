# Generated by Django 2.0.6 on 2018-10-29 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseApp', '0019_transactionmodel_reason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionmodel',
            name='reason',
        ),
        migrations.AddField(
            model_name='expensemodel',
            name='reason',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]