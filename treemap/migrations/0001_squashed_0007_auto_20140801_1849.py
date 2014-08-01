# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [('treemap', '0001_initial'), ('treemap', '0002_remove_trees_owner'), ('treemap', '0003_auto_20140731_2056'), ('treemap', '0004_auto_20140731_2119'), ('treemap', '0005_auto_20140801_1336'), ('treemap', '0006_auto_20140801_1338'), ('treemap', '0007_auto_20140801_1849')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Harbord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('Street', models.CharField(null=True, max_length=255)),
                ('HouseNumber', models.CharField(null=True, max_length=255)),
                ('CommonSpeciesNames', models.CharField(max_length=255)),
                ('Circumference', models.CharField(max_length=255)),
                ('DBH', models.CharField(max_length=255)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='harbord',
            unique_together=set([('Street', 'HouseNumber', 'CommonSpeciesNames', 'Circumference', 'DBH', 'point')]),
        ),
        migrations.CreateModel(
            name='Trees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('address_po', models.IntegerField()),
                ('address_fu', models.CharField(max_length=131)),
                ('objectid', models.IntegerField()),
                ('struct_id', models.CharField(max_length=20)),
                ('common_nam', models.CharField(max_length=254)),
                ('botanical_field', models.CharField(max_length=254)),
                ('diameter_b', models.IntegerField()),
                ('tree_posit', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='trees',
            unique_together=set([('address_po', 'struct_id', 'objectid')]),
        ),
        migrations.RemoveField(
            model_name='trees',
            name='owner',
        ),
        migrations.CreateModel(
            name='HistoricalTrees',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
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
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'historical trees',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
    ]
