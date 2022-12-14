# Generated by Django 4.0.5 on 2022-07-27 21:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0005_alter_executor_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executor',
            name='phone_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+375\\d{9}$')]),
        ),
    ]
