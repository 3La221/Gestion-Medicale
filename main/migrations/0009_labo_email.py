# Generated by Django 5.0.2 on 2024-02-18 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_labo_patients_alter_report_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='labo',
            name='email',
            field=models.EmailField(max_length=255, null=True, unique=True),
        ),
    ]
