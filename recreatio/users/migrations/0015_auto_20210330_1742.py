# Generated by Django 3.0.1 on 2021-03-30 17:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0014_auto_20210328_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activities',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='activities',
            name='title',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activities',
            name='age_group_old',
            field=models.IntegerField(default=20, verbose_name='Oldest Age'),
        ),
        migrations.AlterField(
            model_name='activities',
            name='age_group_young',
            field=models.IntegerField(default=0, verbose_name='Youngest Age'),
        ),
        migrations.AlterField(
            model_name='activities',
            name='max_size',
            field=models.IntegerField(default=0, verbose_name='Registration Maximum'),
        ),
        migrations.AlterField(
            model_name='activities',
            name='reg_end',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 17, 41, 12, 506907, tzinfo=utc), verbose_name='Registration End Time'),
        ),
        migrations.AlterField(
            model_name='activities',
            name='reg_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 17, 41, 12, 506862, tzinfo=utc), verbose_name='Registration Start Time'),
        ),
        migrations.AlterField(
            model_name='activities',
            name='registrant',
            field=models.ManyToManyField(blank=True, to='users.Child'),
        ),
    ]