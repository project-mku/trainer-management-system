# Generated by Django 5.1.1 on 2024-10-04 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_trainer_on_payroll'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='month',
            field=models.CharField(blank=True, choices=[('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], help_text='Month of the payroll', max_length=10, null=True),
        ),
    ]
