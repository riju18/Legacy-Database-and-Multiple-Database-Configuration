# Generated by Django 2.2 on 2021-05-26 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0008_auto_20210526_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]