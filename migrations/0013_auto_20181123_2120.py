# Generated by Django 2.1.3 on 2018-11-23 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20181123_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='location',
            field=models.ForeignKey(on_delete='CASCADE', related_name='events_in_here', to='polls.Locations'),
        ),
    ]
