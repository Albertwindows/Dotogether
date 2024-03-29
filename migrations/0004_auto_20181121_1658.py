# Generated by Django 2.1.3 on 2018-11-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_testclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='users',
            name='uage',
            field=models.PositiveIntegerField(default=18, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='uemail',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
