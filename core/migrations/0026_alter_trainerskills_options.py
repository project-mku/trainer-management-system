# Generated by Django 5.1.1 on 2024-10-22 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_trainerskills_created_trainerskills_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainerskills',
            options={'ordering': ['created'], 'verbose_name': 'Trainer Skill', 'verbose_name_plural': 'Trainer Skills'},
        ),
    ]