# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treemap', '0003_auto_20140731_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaltrees',
            old_name='user_id',
            new_name='changed_by_id',
        ),
        migrations.RenameField(
            model_name='trees',
            old_name='user',
            new_name='changed_by',
        ),
    ]
