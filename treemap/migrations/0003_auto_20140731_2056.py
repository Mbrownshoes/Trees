# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treemap', '0002_remove_trees_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTrees',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True, verbose_name='ID', auto_created=True)),
                ('user_id', models.IntegerField(editable=False, null=True, blank=True, db_index=True)),
                ('address_po', models.IntegerField()),
                ('address_fu', models.CharField(max_length=131)),
                ('objectid', models.IntegerField()),
                ('struct_id', models.CharField(max_length=20)),
                ('common_nam', models.CharField(max_length=254)),
                ('botanical_field', models.CharField(max_length=254)),
                ('diameter_b', models.IntegerField()),
                ('tree_posit', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
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
            name='user',
            field=models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
