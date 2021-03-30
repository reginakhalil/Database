# Generated by Django 3.2.dev20210102203948 on 2021-03-25 13:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210325_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='leaders',
            field=models.ManyToManyField(to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='activities',
            name='reg_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 13, 21, 22, 693471, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activities',
            name='reg_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 13, 21, 22, 693471, tzinfo=utc)),
        ),
    ]