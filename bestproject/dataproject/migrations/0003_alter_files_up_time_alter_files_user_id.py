# Generated by Django 4.1.7 on 2023-03-23 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataproject', '0002_files_user_id_alter_files_up_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='up_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 21, 7, 17, 866241)),
        ),
        migrations.AlterField(
            model_name='files',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
