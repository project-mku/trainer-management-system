# Generated by Django 5.1.1 on 2024-10-11 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_trainer_created_at_trainer_updated_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
