# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.image'
        db.add_column('blogengine_post', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.image'
        db.delete_column('blogengine_post', 'image')


    models = {
        'blogengine.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        'blogengine.post': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Post'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogengine.Category']", 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'default': "''"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['blogengine.Tag']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'text_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'text_fr': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'default': "''", 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'default': "''", 'blank': 'True'})
        },
        'blogengine.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['blogengine']