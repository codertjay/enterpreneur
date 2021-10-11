# Generated by Django 3.0.3 on 2020-05-02 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coding', '0011_auto_20200502_2350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='time',
            new_name='created_on',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='user',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coding.BlogPost'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='username',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]