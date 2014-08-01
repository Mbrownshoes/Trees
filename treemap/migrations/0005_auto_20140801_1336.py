# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemap', '0004_auto_20140731_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaltrees',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalTrees',
        ),
        migrations.RemoveField(
            model_name='trees',
            name='changed_by',
        ),
    ]
