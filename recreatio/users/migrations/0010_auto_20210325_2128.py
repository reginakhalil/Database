# Generated by Django 3.2.dev20210102203948 on 2021-03-26 01:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210325_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='reg_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 1, 28, 16, 580743, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activities',
            name='reg_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 1, 28, 16, 580743, tzinfo=utc)),
        ),
    ]