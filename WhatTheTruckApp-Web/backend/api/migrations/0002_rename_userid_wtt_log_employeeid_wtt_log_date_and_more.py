# Generated by Django 5.1.6 on 2025-03-05 01:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wtt_log',
            old_name='userID',
            new_name='employeeID',
        ),
        migrations.AddField(
            model_name='wtt_log',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='wtt_trailer',
            name='trailerID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wtt_truck',
            name='truckID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wtt_user',
            name='employeeID',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
