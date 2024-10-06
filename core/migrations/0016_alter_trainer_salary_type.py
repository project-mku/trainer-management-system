# Generated by Django 5.1.1 on 2024-10-04 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_trainer_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='salary_type',
            field=models.CharField(choices=[('fixed', 'Fixed Salary'), ('hourly', 'Hourly Rate')], default='fixed', help_text='How would you like to be paid?', max_length=6),
        ),
    ]
