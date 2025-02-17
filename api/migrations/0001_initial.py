# Generated by Django 5.0.4 on 2024-05-07 19:53

import django.db.models.deletion
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
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
            },
        ),
        migrations.CreateModel(
            name='Specialties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('date_now', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.doctor')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.specialties'),
        ),
    ]
