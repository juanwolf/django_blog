# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.keywords'
        db.add_column('blogengine_post', 'keywords',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Post.image'
        db.alter_column('blogengine_post', 'image', self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100))

    def backwards(self, orm):
        # Deleting field 'Post.keywords'
        db.delete_column('blogengine_post', 'keywords')


        # Changing field 'Post.image'
        db.alter_column('blogengine_post', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        'blogengine.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'null': 'True', 'unique': 'True', 'blank': 'True', 'max_length': '40'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'null': 'True', 'unique': 'True', 'blank': 'True', 'max_length': '40'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'null': 'True', 'unique': 'True', 'blank': 'True', 'max_length': '40'})
        },
        'blogengine.post': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Post'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogengine.Category']", 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'null': 'True', 'unique': 'True', 'blank': 'True', 'max_length': '50'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'null': 'True', 'unique': 'True', 'blank': 'True', 'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['blogengine.Tag']", 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'default': "''"}),
            'text_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'title_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'default': "''", 'max_length': '200'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'default': "''", 'max_length': '200'})
        },
        'blogengine.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'null': 'True', 'unique': 'True', 'blank': 'True', 'max_length': '40'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'null': 'True', 'unique': 'True', 'blank': 'True', 'max_length': '40'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'null': 'True', 'unique': 'True', 'blank': 'True', 'max_length': '40'})
        }
    }

    complete_apps = ['blogengine']