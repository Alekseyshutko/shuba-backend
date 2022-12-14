# Generated by Django 4.0.5 on 2022-07-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderphotos'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialityOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'specialityorder',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='speciality',
            field=models.ManyToManyField(to='order.specialityorder'),
        ),
    ]
