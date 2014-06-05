# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.slug'
        db.add_column('blogengine_category', 'slug',
                      self.gf('django.db.models.fields.SlugField')(unique=True, null=True, max_length=40, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.slug'
        db.delete_column('blogengine_category', 'slug')


    models = {
        'blogengine.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'null': 'True', 'max_length': '40', 'blank': 'True'})
        },
        'blogengine.post': {
            'Meta': {'object_name': 'Post', 'ordering': "['-pub_date']"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['blogengine.Category']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        }
    }

    complete_apps = ['blogengine']