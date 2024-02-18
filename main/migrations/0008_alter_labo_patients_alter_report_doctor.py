# Generated by Django 5.0.2 on 2024-02-18 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_doctor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labo',
            name='patients',
            field=models.ManyToManyField(blank=True, null=True, related_name='Labo', to='main.profile'),
        ),
        migrations.AlterField(
            model_name='report',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='main.doctor'),
        ),
    ]
