# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemap', '0006_auto_20140801_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaltrees',
            name='changed_by_id',
        ),
        migrations.RemoveField(
            model_name='trees',
            name='changed_by',
        ),
    ]
