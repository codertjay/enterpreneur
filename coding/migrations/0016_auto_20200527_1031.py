# Generated by Django 3.0.3 on 2020-05-27 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0015_auto_20200527_1029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='username',
            new_name='user',
        ),
    ]
