# Generated by Django 5.0.2 on 2024-02-18 20:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_doctor_patients_remove_labo_patients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
