# Generated by Django 3.2.dev20210102203948 on 2021-03-26 01:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210325_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activities',
            name='activities',
        ),
        migrations.AlterField(
            model_name='activities',
            name='reg_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 1, 40, 31, 504568, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activities',
            name='reg_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 1, 40, 31, 504568, tzinfo=utc)),
        ),
    ]
