# Generated by Django 4.2.1 on 2023-05-13 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testsession',
            name='is_finished',
        ),
    ]