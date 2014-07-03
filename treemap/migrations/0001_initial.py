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

        # Adding model 'Harbord'
        db.create_table(u'treemap_harbord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('HouseNumber', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('CommonSpeciesNames', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Circumference', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('DBH', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'treemap', ['Harbord'])

        # Adding model 'UserProfile'
        db.create_table(u'treemap_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'treemap', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'Trees'
        db.delete_table(u'treemap_trees')

        # Deleting model 'Harbord'
        db.delete_table(u'treemap_harbord')

        # Deleting model 'UserProfile'
        db.delete_table(u'treemap_userprofile')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'treemap.harbord': {
            'Circumference': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'CommonSpeciesNames': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'DBH': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'HouseNumber': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'Meta': {'object_name': 'Harbord'},
            'Street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
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
        },
        u'treemap.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['treemap']