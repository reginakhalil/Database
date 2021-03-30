# Generated by Django 3.2.dev20210102203948 on 2021-03-26 01:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210325_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='activities',
        ),
        migrations.AddField(
            model_name='activities',
            name='organization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.organization'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activities',
            name='reg_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 1, 39, 17, 751594, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activities',
            name='reg_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 1, 39, 17, 751594, tzinfo=utc)),
        ),
    ]
