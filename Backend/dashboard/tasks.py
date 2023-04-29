from __future__ import absolute_import, unicode_literals

from datetime import datetime

from celery import shared_task

from .models import ToDoList


@shared_task
def add(x, y):
    return x + y


@shared_task
def to_do_remove():
    today = today = datetime.now().date()
    expired = ToDoList.objects.filter(created__lt=today)
    return expired.delete()
