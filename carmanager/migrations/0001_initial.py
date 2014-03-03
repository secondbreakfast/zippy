# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Car'
        db.create_table(u'carmanager_car', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('horsepower', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('transmission', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('gears', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'carmanager', ['Car'])


    def backwards(self, orm):
        # Deleting model 'Car'
        db.delete_table(u'carmanager_car')


    models = {
        u'carmanager.car': {
            'Meta': {'object_name': 'Car'},
            'gears': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'horsepower': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'transmission': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['carmanager']