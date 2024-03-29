# Generated by Django 2.1.3 on 2018-11-22 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_users_upassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('event_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='users',
            old_name='uage',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='uemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='uname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='upassword',
            new_name='password',
        ),
        migrations.AddField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='initiator',
            field=models.ForeignKey(on_delete='CASCADE', related_name='initiator', to='polls.Users'),
        ),
        migrations.AddField(
            model_name='events',
            name='location',
            field=models.ForeignKey(on_delete='CASCADE', related_name='location', to='polls.Locations'),
        ),
    ]
