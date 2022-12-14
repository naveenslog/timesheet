# Generated by Django 4.0.6 on 2022-09-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='in_time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='out_time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]
