# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 08:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20160303_0558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskanswer',
            name='task',
        ),
        migrations.RemoveField(
            model_name='taskanswer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usertask',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='usertask',
            name='tasks',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='TaskAnswer',
        ),
        migrations.DeleteModel(
            name='UserTask',
        ),
    ]
