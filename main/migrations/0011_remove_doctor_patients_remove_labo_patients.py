# Generated by Django 5.0.2 on 2024-02-18 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_labo_radio_labo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='patients',
        ),
        migrations.RemoveField(
            model_name='labo',
            name='patients',
        ),
    ]