# Generated by Django 5.1.1 on 2024-10-01 05:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_payment_payment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payslip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('gross_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deductions', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('net_salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Payslip',
                'verbose_name_plural': 'Payslips',
            },
        ),
        migrations.RemoveIndex(
            model_name='payment',
            name='core_paymen_student_d9e3a9_idx',
        ),
        migrations.RemoveIndex(
            model_name='payroll',
            name='core_payrol_trainer_748ad8_idx',
        ),
        migrations.AlterField(
            model_name='payroll',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('cancelled', 'Cancelled')], default='pending', max_length=10),
        ),
        migrations.AddField(
            model_name='payslip',
            name='payment_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.paymentmethod'),
        ),
        migrations.AddField(
            model_name='payslip',
            name='payroll',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.payroll'),
        ),
        migrations.AddField(
            model_name='payslip',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trainer'),
        ),
    ]
