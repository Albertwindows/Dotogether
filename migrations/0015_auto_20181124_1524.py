# Generated by Django 2.1.3 on 2018-11-24 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_events_submit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 15, 24, 8, 53356)),
        ),
    ]
