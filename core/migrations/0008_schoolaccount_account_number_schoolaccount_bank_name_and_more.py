# Generated by Django 5.1.1 on 2024-10-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_payslip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolaccount',
            name='account_number',
            field=models.CharField(default='1234567890', max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='schoolaccount',
            name='bank_name',
            field=models.CharField(default='Example Bank', max_length=100),
        ),
        migrations.AddField(
            model_name='schoolaccount',
            name='branch',
            field=models.CharField(default='Main Branch', max_length=100),
        ),
        migrations.AddField(
            model_name='schoolaccount',
            name='branch_code',
            field=models.CharField(default='001', max_length=10),
        ),
    ]
