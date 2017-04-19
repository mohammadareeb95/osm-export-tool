# noqa
# -*- coding: utf-8 -*-

from datetime import datetime

from django.utils import timezone
import pytz

from core.celery import app
from jobs.models import HDXExportRegion

from .task_runners import ExportTaskRunner


@app.task(name='Queue Periodic Runs')
def queue_periodic_job_runs(): # noqa
    now = timezone.now()

    for region in HDXExportRegion.objects.exclude(schedule_period='disabled'):
        last_run = region.job.runs.last()
        if last_run:
            last_run_at = last_run.created_at
        else:
            last_run_at = datetime.fromtimestamp(0, pytz.timezone('UTC'))

        if (now - last_run_at > region.delta) or \
            (region.schedule_period == '6hrs' and
                (now.hour - region.schedule_hour) % 6 == 0) or \
            (region.schedule_period == 'daily' and
                region.schedule_hour == now.hour) or \
            (region.schedule_period == 'weekly' and
                (now.weekday() + 1) % 7 == 0 and
                region.schedule_hour == now.hour) or \
            (region.schedule_period == 'monthly' and
                now.day == 1 and
                region.schedule_hour == now.hour):
            ExportTaskRunner().run_task(job_uid=region.job.uid)
