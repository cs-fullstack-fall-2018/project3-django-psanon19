# Generated by Django 2.0.6 on 2018-10-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseApp', '0011_auto_20181026_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='deposits',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='withdraws',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
