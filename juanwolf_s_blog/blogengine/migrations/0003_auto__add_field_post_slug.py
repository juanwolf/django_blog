# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.slug'
        db.add_column('blogengine_post', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=40, unique=True, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.slug'
        db.delete_column('blogengine_post', 'slug')


    models = {
        'blogengine.post': {
            'Meta': {'object_name': 'Post', 'ordering': "['-pub_date']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'unique': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"})
        }
    }

    complete_apps = ['blogengine']