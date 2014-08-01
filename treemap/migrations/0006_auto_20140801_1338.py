# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treemap', '0005_auto_20140801_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTrees',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', auto_created=True, blank=True)),
                ('address_po', models.IntegerField()),
                ('address_fu', models.CharField(max_length=131)),
                ('objectid', models.IntegerField()),
                ('struct_id', models.CharField(max_length=20)),
                ('common_nam', models.CharField(max_length=254)),
                ('botanical_field', models.CharField(max_length=254)),
                ('diameter_b', models.IntegerField()),
                ('tree_posit', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('changed_by_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical trees',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='trees',
            name='changed_by',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
