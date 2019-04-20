# -*- coding: utf-8 -*-


from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab


app = Celery('proj',
             broker='redis://192.168.1.101',
             backend='redis://192.168.1.101',
             include=['proj.tasks']
      )

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-minute': {
        'task': 'tasks.add',
        #  'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'schedule': crontab(minute='*'),
        'args': (50, 100),
    },
}

app.conf.timezone = 'UTC'


if __name__ == '__main__':
    app.start()

