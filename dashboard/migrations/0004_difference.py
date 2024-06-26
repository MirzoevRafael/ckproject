# Generated by Django 5.0.6 on 2024-06-04 17:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Difference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2024)])),
                ('economic_activity', models.CharField(max_length=500)),
                ('total', models.IntegerField()),
            ],
        ),
    ]
