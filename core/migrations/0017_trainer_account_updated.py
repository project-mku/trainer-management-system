# Generated by Django 5.1.1 on 2024-10-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_trainer_salary_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='account_updated',
            field=models.BooleanField(default=False),
        ),
    ]