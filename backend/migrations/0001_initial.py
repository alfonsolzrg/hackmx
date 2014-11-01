# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Citizen'
        db.create_table(u'backend_citizen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('backend', ['Citizen'])

        # Adding model 'Event'
        db.create_table(u'backend_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=8)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=8)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('up_votes', self.gf('django.db.models.fields.IntegerField')()),
            ('down_votes', self.gf('django.db.models.fields.IntegerField')()),
            ('citizen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Citizen'], null=True, blank=True)),
            ('reported_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('gravity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('backend', ['Event'])

        # Adding model 'EventUpvote'
        db.create_table(u'backend_eventupvote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Event'])),
            ('citizen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Citizen'])),
            ('up_vote', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('backend', ['EventUpvote'])


    def backwards(self, orm):
        # Deleting model 'Citizen'
        db.delete_table(u'backend_citizen')

        # Deleting model 'Event'
        db.delete_table(u'backend_event')

        # Deleting model 'EventUpvote'
        db.delete_table(u'backend_eventupvote')


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
        'backend.citizen': {
            'Meta': {'object_name': 'Citizen'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'backend.event': {
            'Meta': {'object_name': 'Event'},
            'citizen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Citizen']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'down_votes': ('django.db.models.fields.IntegerField', [], {}),
            'gravity': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '8'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '8'}),
            'reported_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'up_votes': ('django.db.models.fields.IntegerField', [], {})
        },
        'backend.eventupvote': {
            'Meta': {'object_name': 'EventUpvote'},
            'citizen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Citizen']"}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'up_vote': ('django.db.models.fields.BooleanField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['backend']