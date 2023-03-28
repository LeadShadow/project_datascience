# Generated by Django 4.1.7 on 2023-03-24 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataproject', '0004_remove_files_name_remove_files_type_files_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('up_time', models.DateTimeField(default=datetime.datetime(2023, 3, 24, 19, 34, 41, 933655))),
            ],
        ),
        migrations.DeleteModel(
            name='Files',
        ),
    ]
