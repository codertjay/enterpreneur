# Generated by Django 3.0.3 on 2020-04-27 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='users',
        ),
    ]
