# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_task_usertask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_file',
        ),
        migrations.AddField(
            model_name='task',
            name='Task <built-in function id>',
            field=models.FileField(blank=True, null=True, upload_to=b'tasks/problems/'),
        ),
        migrations.AddField(
            model_name='task',
            name='for_lecture',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usertask',
            name='answer_file',
            field=models.FileField(blank=True, null=True, upload_to=b"tasks/solutions/<class 'django.contrib.auth.models.User'>"),
        ),
        migrations.AlterField(
            model_name='usertask',
            name='mark',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
