# Generated by Django 4.0.6 on 2022-08-03 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_user_is_online_user_verify_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_online',
        ),
        migrations.RemoveField(
            model_name='user',
            name='verify_code',
        ),
    ]