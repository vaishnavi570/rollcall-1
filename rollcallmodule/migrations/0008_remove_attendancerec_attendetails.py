# Generated by Django 3.0.8 on 2020-08-01 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rollcallmodule', '0007_auto_20200730_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancerec',
            name='attendetails',
        ),
    ]
