# Generated by Django 3.0.8 on 2020-07-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rollcallmodule', '0004_attendancerec_matchrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerec',
            name='matchrate',
            field=models.CharField(default=0, max_length=45),
        ),
    ]
