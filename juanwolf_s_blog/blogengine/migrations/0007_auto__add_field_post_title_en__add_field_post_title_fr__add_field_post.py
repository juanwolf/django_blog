# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.title_en'
        db.add_column('blogengine_post', 'title_en',
                      self.gf('django.db.models.fields.CharField')(default='', null=True, max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Post.title_fr'
        db.add_column('blogengine_post', 'title_fr',
                      self.gf('django.db.models.fields.CharField')(default='', null=True, max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Post.text_en'
        db.add_column('blogengine_post', 'text_en',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.text_fr'
        db.add_column('blogengine_post', 'text_fr',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.slug_en'
        db.add_column('blogengine_post', 'slug_en',
                      self.gf('django.db.models.fields.SlugField')(unique=True, null=True, max_length=40, blank=True),
                      keep_default=False)

        # Adding field 'Post.slug_fr'
        db.add_column('blogengine_post', 'slug_fr',
                      self.gf('django.db.models.fields.SlugField')(unique=True, null=True, max_length=40, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.title_en'
        db.delete_column('blogengine_post', 'title_en')

        # Deleting field 'Post.title_fr'
        db.delete_column('blogengine_post', 'title_fr')

        # Deleting field 'Post.text_en'
        db.delete_column('blogengine_post', 'text_en')

        # Deleting field 'Post.text_fr'
        db.delete_column('blogengine_post', 'text_fr')

        # Deleting field 'Post.slug_en'
        db.delete_column('blogengine_post', 'slug_en')

        # Deleting field 'Post.slug_fr'
        db.delete_column('blogengine_post', 'slug_fr')


    models = {
        'blogengine.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'null': 'True', 'max_length': '40', 'blank': 'True'})
        },
        'blogengine.post': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Post'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogengine.Category']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'null': 'True', 'max_length': '40', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'null': 'True', 'max_length': '40', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blogengine.Tag']", 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'text_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'text_fr': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'title_en': ('django.db.models.fields.CharField', [], {'default': "''", 'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'default': "''", 'null': 'True', 'max_length': '200', 'blank': 'True'})
        },
        'blogengine.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'null': 'True', 'max_length': '40', 'blank': 'True'})
        }
    }

    complete_apps = ['blogengine']