# Generated by Django 2.2 on 2021-05-19 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_auto_20210519_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]