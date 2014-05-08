# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trees'
        db.create_table(u'treemap_trees', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address_po', self.gf('django.db.models.fields.IntegerField')()),
            ('address_fu', self.gf('django.db.models.fields.CharField')(max_length=131)),
            ('objectid', self.gf('django.db.models.fields.IntegerField')()),
            ('struct_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('common_nam', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('botanical_field', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('diameter_b', self.gf('django.db.models.fields.IntegerField')()),
            ('tree_posit', self.gf('django.db.models.fields.IntegerField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPointField')()),
        ))
        db.send_create_signal(u'treemap', ['Trees'])


    def backwards(self, orm):
        # Deleting model 'Trees'
        db.delete_table(u'treemap_trees')


    models = {
        u'treemap.trees': {
            'Meta': {'object_name': 'Trees'},
            'address_fu': ('django.db.models.fields.CharField', [], {'max_length': '131'}),
            'address_po': ('django.db.models.fields.IntegerField', [], {}),
            'botanical_field': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'common_nam': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'diameter_b': ('django.db.models.fields.IntegerField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objectid': ('django.db.models.fields.IntegerField', [], {}),
            'struct_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tree_posit': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['treemap']