# Generated by Django 2.1.3 on 2018-11-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20181121_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='upassword',
            field=models.CharField(default='123456', max_length=40),
        ),
    ]
