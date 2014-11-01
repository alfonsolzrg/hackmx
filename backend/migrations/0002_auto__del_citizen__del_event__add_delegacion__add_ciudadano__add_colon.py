# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Citizen'
        db.delete_table(u'backend_citizen')

        # Deleting model 'Event'
        db.delete_table(u'backend_event')

        # Adding model 'Delegacion'
        db.create_table(u'backend_delegacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('backend', ['Delegacion'])

        # Adding model 'Ciudadano'
        db.create_table(u'backend_ciudadano', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('backend', ['Ciudadano'])

        # Adding model 'Colonia'
        db.create_table(u'backend_colonia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('codigo_postal', self.gf('django.db.models.fields.IntegerField')()),
            ('delegacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Delegacion'])),
        ))
        db.send_create_signal('backend', ['Colonia'])

        # Adding model 'Evento'
        db.create_table(u'backend_evento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('latitud', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=8)),
            ('longitud', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=8)),
            ('colonia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Colonia'])),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('votos', self.gf('django.db.models.fields.IntegerField')()),
            ('ciudadano', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Ciudadano'], null=True, blank=True)),
            ('fecha_reporte', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('gravedad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('backend', ['Evento'])

        # Deleting field 'EventUpvote.up_vote'
        db.delete_column(u'backend_eventupvote', 'up_vote')

        # Deleting field 'EventUpvote.event'
        db.delete_column(u'backend_eventupvote', 'event_id')

        # Deleting field 'EventUpvote.citizen'
        db.delete_column(u'backend_eventupvote', 'citizen_id')

        # Adding field 'EventUpvote.evento'
        db.add_column(u'backend_eventupvote', 'evento',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['backend.Evento']),
                      keep_default=False)

        # Adding field 'EventUpvote.ciudadano'
        db.add_column(u'backend_eventupvote', 'ciudadano',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['backend.Ciudadano']),
                      keep_default=False)

        # Adding field 'EventUpvote.fecha_voto'
        db.add_column(u'backend_eventupvote', 'fecha_voto',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Citizen'
        db.create_table(u'backend_citizen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('backend', ['Citizen'])

        # Adding model 'Event'
        db.create_table(u'backend_event', (
            ('reported_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('up_votes', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gravity', self.gf('django.db.models.fields.IntegerField')()),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=8)),
            ('down_votes', self.gf('django.db.models.fields.IntegerField')()),
            ('citizen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Citizen'], null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=8)),
        ))
        db.send_create_signal('backend', ['Event'])

        # Deleting model 'Delegacion'
        db.delete_table(u'backend_delegacion')

        # Deleting model 'Ciudadano'
        db.delete_table(u'backend_ciudadano')

        # Deleting model 'Colonia'
        db.delete_table(u'backend_colonia')

        # Deleting model 'Evento'
        db.delete_table(u'backend_evento')

        # Adding field 'EventUpvote.up_vote'
        db.add_column(u'backend_eventupvote', 'up_vote',
                      self.gf('django.db.models.fields.BooleanField')(default=0),
                      keep_default=False)

        # Adding field 'EventUpvote.event'
        db.add_column(u'backend_eventupvote', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['backend.Event']),
                      keep_default=False)

        # Adding field 'EventUpvote.citizen'
        db.add_column(u'backend_eventupvote', 'citizen',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['backend.Citizen']),
                      keep_default=False)

        # Deleting field 'EventUpvote.evento'
        db.delete_column(u'backend_eventupvote', 'evento_id')

        # Deleting field 'EventUpvote.ciudadano'
        db.delete_column(u'backend_eventupvote', 'ciudadano_id')

        # Deleting field 'EventUpvote.fecha_voto'
        db.delete_column(u'backend_eventupvote', 'fecha_voto')


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
        'backend.ciudadano': {
            'Meta': {'object_name': 'Ciudadano'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'backend.colonia': {
            'Meta': {'object_name': 'Colonia'},
            'codigo_postal': ('django.db.models.fields.IntegerField', [], {}),
            'delegacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Delegacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'backend.delegacion': {
            'Meta': {'object_name': 'Delegacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'backend.evento': {
            'Meta': {'object_name': 'Evento'},
            'ciudadano': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Ciudadano']", 'null': 'True', 'blank': 'True'}),
            'colonia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Colonia']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha_reporte': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gravedad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '8'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '8'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'votos': ('django.db.models.fields.IntegerField', [], {})
        },
        'backend.eventupvote': {
            'Meta': {'object_name': 'EventUpvote'},
            'ciudadano': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Ciudadano']"}),
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Evento']"}),
            'fecha_voto': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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