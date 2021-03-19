# Generated by Django 3.2.dev20210102203948 on 2021-03-19 00:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activities', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('age_group_young', models.IntegerField()),
                ('age_group_old', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='child',
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=40)),
                ('activities', models.ManyToManyField(to='users.Activities')),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('activity_list', models.ManyToManyField(to='users.Activities')),
                ('parent', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]