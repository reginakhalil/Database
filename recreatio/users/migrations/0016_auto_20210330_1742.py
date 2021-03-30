# Generated by Django 3.0.1 on 2021-03-30 17:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20210330_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='reg_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 17, 42, 39, 452981, tzinfo=utc), verbose_name='Registration End Time'),
        ),
        migrations.AlterField(
            model_name='activities',
            name='reg_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 17, 42, 39, 452941, tzinfo=utc), verbose_name='Registration Start Time'),
        ),
    ]
