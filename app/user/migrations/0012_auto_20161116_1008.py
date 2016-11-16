# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-16 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20160905_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_file',
            field=models.FileField(blank=True, null=True, upload_to='tasks/problems/'),
        ),
        migrations.AlterField(
            model_name='taskanswer',
            name='answer_file',
            field=models.FileField(blank=True, null=True, upload_to='tasks/solutions/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='group',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
