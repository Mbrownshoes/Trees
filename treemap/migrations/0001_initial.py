# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Harbord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Street', models.CharField(max_length=255, null=True)),
                ('HouseNumber', models.CharField(max_length=255, null=True)),
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
            name='HistoricalTrees',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', blank=True, auto_created=True, db_index=True)),
                ('address_po', models.IntegerField()),
                ('address_fu', models.CharField(max_length=131)),
                ('objectid', models.IntegerField()),
                ('struct_id', models.CharField(max_length=20)),
                ('common_nam', models.CharField(max_length=254)),
                ('botanical_field', models.CharField(max_length=254)),
                ('diameter_b', models.IntegerField()),
                ('tree_posit', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical trees',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('address_po', models.IntegerField()),
                ('address_fu', models.CharField(max_length=131)),
                ('objectid', models.IntegerField()),
                ('struct_id', models.CharField(max_length=20)),
                ('common_nam', models.CharField(max_length=254)),
                ('botanical_field', models.CharField(max_length=254)),
                ('diameter_b', models.IntegerField()),
                ('tree_posit', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='trees',
            unique_together=set([('address_po', 'struct_id', 'objectid')]),
        ),
    ]
