# -*- coding: utf8 -*-
from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=128)
    individual = models.BooleanField()
    for_lecture = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField()
    task_file = models.FileField(
        blank=True,
        null=True,
        upload_to="tasks/problems/"
    )
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return u'Task %s (%s)' % (self.id, self.title)


class TaskAnswer(models.Model):
    task = models.OneToOneField(Task)
    user = models.OneToOneField(User)
    answer_file = models.FileField(blank=True, null=True,
                                   upload_to="tasks/solutions/" + str(User))
    mark = models.PositiveSmallIntegerField(blank=True, null=True)
