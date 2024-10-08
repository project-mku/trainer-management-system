# Generated by Django 5.1.1 on 2024-10-01 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_schoolaccount_alter_trainer_base_salary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='payment_type',
            field=models.CharField(choices=[('bank', 'Bank Transfer'), ('mpesa', 'Mpesa'), ('check', 'Check'), ('cash', 'Cash')], max_length=6),
        ),
    ]
