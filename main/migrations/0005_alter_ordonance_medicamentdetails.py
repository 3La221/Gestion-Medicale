# Generated by Django 5.0.2 on 2024-02-18 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_maladie_medicament_doctor_isprivee_medicamentdetails_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordonance',
            name='medicamentDetails',
            field=models.ManyToManyField(to='main.medicamentdetails'),
        ),
    ]
