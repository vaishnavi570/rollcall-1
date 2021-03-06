# Generated by Django 3.0.7 on 2020-07-13 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rollcallmodule', '0002_auto_20200713_1700'),
        ('usermgnt', '0002_auto_20200708_0410'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=45)),
                ('Password', models.CharField(max_length=45)),
                ('StudID', models.ForeignKey(db_column='studetails', on_delete=django.db.models.deletion.CASCADE, to='rollcallmodule.attendancerec')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.DeleteModel(
            name='AdminInfo',
        ),
        migrations.DeleteModel(
            name='StudentInfo',
        ),
    ]
