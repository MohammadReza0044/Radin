from __future__ import absolute_import, unicode_literals

from datetime import datetime

from celery import shared_task

from .models import Contract


@shared_task
def delay_calculate():
    pass
