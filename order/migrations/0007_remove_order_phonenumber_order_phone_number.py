# Generated by Django 4.0.5 on 2022-07-28 19:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phoneNumber',
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='SOME STRING', max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+375\\d{9}$')]),
        ),
    ]