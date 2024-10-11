# Generated by Django 5.1.1 on 2024-10-10 17:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_trainer_trainer_status_alter_trainer_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
