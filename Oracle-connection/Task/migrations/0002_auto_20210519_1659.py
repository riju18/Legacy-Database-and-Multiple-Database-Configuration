# Generated by Django 2.2 on 2021-05-19 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('-id',)},
        ),
    ]
