# Generated by Django 4.1.7 on 2023-03-23 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataproject', '0003_alter_files_up_time_alter_files_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='name',
        ),
        migrations.RemoveField(
            model_name='files',
            name='type',
        ),
        migrations.AddField(
            model_name='files',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='files',
            name='up_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 21, 13, 0, 607339)),
        ),
    ]
