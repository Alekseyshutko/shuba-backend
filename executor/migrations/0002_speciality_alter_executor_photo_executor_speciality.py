# Generated by Django 4.0.5 on 2022-06-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'speciality',
            },
        ),
        migrations.AlterField(
            model_name='executor',
            name='photo',
            field=models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='executor',
            name='speciality',
            field=models.ManyToManyField(to='executor.speciality'),
        ),
    ]
