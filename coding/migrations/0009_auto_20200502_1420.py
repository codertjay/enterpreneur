# Generated by Django 3.0.3 on 2020-05-02 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0008_auto_20200429_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='users',
            new_name='user',
        ),
    ]
