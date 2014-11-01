# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Colonia'
        db.delete_table(u'backend_colonia')

        # Adding model 'TipoLugar'
        db.create_table(u'backend_tipolugar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('backend', ['TipoLugar'])

        # Adding model 'Lugar'
        db.create_table(u'backend_lugar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.TipoLugar'])),
            ('codigo_postal', self.gf('django.db.models.fields.IntegerField')()),
            ('delegacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Delegacion'])),
        ))
        db.send_create_signal('backend', ['Lugar'])

        # Deleting field 'Evento.colonia'
        db.delete_column(u'backend_evento', 'colonia_id')

        # Adding field 'Evento.lugar'
        db.add_column(u'backend_evento', 'lugar',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['backend.Lugar']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Colonia'
        db.create_table(u'backend_colonia', (
            ('codigo_postal', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('delegacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Delegacion'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('backend', ['Colonia'])

        # Deleting model 'TipoLugar'
        db.delete_table(u'backend_tipolugar')

        # Deleting model 'Lugar'
        db.delete_table(u'backend_lugar')

        # Adding field 'Evento.colonia'
        db.add_column(u'backend_evento', 'colonia',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['backend.Colonia']),
                      keep_default=False)

        # Deleting field 'Evento.lugar'
        db.delete_column(u'backend_evento', 'lugar_id')


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
        'backend.delegacion': {
            'Meta': {'object_name': 'Delegacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'backend.evento': {
            'Meta': {'object_name': 'Evento'},
            'ciudadano': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Ciudadano']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha_reporte': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'gravedad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '8'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '8'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Lugar']"}),
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
        'backend.lugar': {
            'Meta': {'object_name': 'Lugar'},
            'codigo_postal': ('django.db.models.fields.IntegerField', [], {}),
            'delegacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.Delegacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend.TipoLugar']"})
        },
        'backend.tipolugar': {
            'Meta': {'object_name': 'TipoLugar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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