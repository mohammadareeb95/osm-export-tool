# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2022-12-03 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0076_remove_hdxexportregion_sync_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hdxexportregion',
            name='schedule_period',
            field=models.CharField(choices=[('6hrs', 'Every 6 hours'), ('daily', 'Every day'), ('weekly', 'Every Sunday'), ('2wks', 'Every two weeks'), ('3wks', 'Every three weeks'), ('monthly', 'The 1st of every month'), ('quarterly', 'Every quarter (90 days)'), ('semiyearly', 'Every 6 months'), ('yearly', 'Every year'), ('disabled', 'Disabled')], default='disabled', max_length=10),
        ),
        migrations.AlterField(
            model_name='partnerexportregion',
            name='schedule_period',
            field=models.CharField(choices=[('6hrs', 'Every 6 hours'), ('daily', 'Every day'), ('weekly', 'Every Sunday'), ('2wks', 'Every two weeks'), ('3wks', 'Every three weeks'), ('monthly', 'The 1st of every month'), ('quarterly', 'Every quarter (90 days)'), ('semiyearly', 'Every 6 months'), ('yearly', 'Every year'), ('disabled', 'Disabled')], default='disabled', max_length=10),
        ),
    ]
