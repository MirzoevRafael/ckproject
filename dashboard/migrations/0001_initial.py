# Generated by Django 5.0.6 on 2024-06-01 19:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2024)])),
                ('economic_activity', models.CharField(max_length=100)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
