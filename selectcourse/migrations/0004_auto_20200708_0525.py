# Generated by Django 3.0.7 on 2020-07-08 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selectcourse', '0003_auto_20200708_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tselectcourse',
            name='tenddate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tselectcourse',
            name='tstartdate',
            field=models.DateTimeField(null=True),
        ),
    ]