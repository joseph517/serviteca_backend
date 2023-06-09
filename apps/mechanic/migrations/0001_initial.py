# Generated by Django 4.0.4 on 2023-05-22 07:43

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(default=None, max_length=255, unique=True)),
                ('name', models.CharField(default=None, max_length=255)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Celular')),
            ],
            options={
                'verbose_name': 'Mecanico',
                'verbose_name_plural': 'Mecanicos',
            },
        ),
    ]
