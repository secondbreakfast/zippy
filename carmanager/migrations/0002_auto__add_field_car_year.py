# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Car.year'
        db.add_column(u'carmanager_car', 'year',
                      self.gf('django.db.models.fields.IntegerField')(default=2014, max_length=4),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Car.year'
        db.delete_column(u'carmanager_car', 'year')


    models = {
        u'carmanager.car': {
            'Meta': {'object_name': 'Car'},
            'gears': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'horsepower': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'transmission': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['carmanager']