# Generated by Django 5.0.2 on 2024-02-17 21:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('bio', models.TextField()),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('specialite', models.CharField(choices=[('CARDIOLOGIE', 'Cardiologie'), ('DERMATOLOGIE', 'Dermatologie'), ('GASTRO_ENTEROLOGIE', 'Gastro-entérologie'), ('NEUROLOGIE', 'Neurologie'), ('PEDIATRIE', 'Pédiatrie'), ('PSYCHIATRIE', 'Psychiatrie'), ('RADIOLOGIE', 'Radiologie'), ('CHIRURGIE', 'Chirurgie'), ('AUTRE', 'Autre')], max_length=50)),
                ('numero_tel', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('carte_id', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date', models.DateField()),
                ('numero_tel', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('blood_type', models.CharField(choices=[('A+', 'A_POSITIVE'), ('A-', 'A_NEGATIVE'), ('B+', 'B_POSITIVE'), ('B-', 'B_NEGATIVE'), ('AB+', 'AB_POSITIVE'), ('AB-', 'AB_NEGATIVE'), ('O+', 'O_POSITIVE'), ('O-', 'O_NEGATIVE')], max_length=3)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('emergency_numbers', models.JSONField(default=list)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
