# Generated by Django 2.1.3 on 2018-11-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20181122_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='sex',
            field=models.CharField(default='男', max_length=2),
        ),
    ]
