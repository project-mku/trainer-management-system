# Generated by Django 5.1.1 on 2024-10-22 07:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_remove_trainer_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainerskills',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainerskills',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
