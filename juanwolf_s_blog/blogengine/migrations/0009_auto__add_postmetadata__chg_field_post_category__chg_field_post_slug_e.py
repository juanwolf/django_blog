# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Changing field 'Post.category'
        db.alter_column('blogengine_post', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogengine.Category']))

        # Changing field 'Post.slug_en'
        db.alter_column('blogengine_post', 'slug_en', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True))

        # Changing field 'Post.slug_fr'
        db.alter_column('blogengine_post', 'slug_fr', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True))

        # Changing field 'Post.slug'
        db.alter_column('blogengine_post', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True))

    def backwards(self, orm):
        # Changing field 'Post.category'
        db.alter_column('blogengine_post', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogengine.Category'], null=True))

        # Changing field 'Post.slug_en'
        db.alter_column('blogengine_post', 'slug_en', self.gf('django.db.models.fields.SlugField')(max_length=40, unique=True, null=True))

        # Changing field 'Post.slug_fr'
        db.alter_column('blogengine_post', 'slug_fr', self.gf('django.db.models.fields.SlugField')(max_length=40, unique=True, null=True))

        # Changing field 'Post.slug'
        db.alter_column('blogengine_post', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=40, unique=True))

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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'blogengine.post': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Post'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['blogengine.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blogengine.Tag']", 'null': 'True', 'blank': 'True', 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'text_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'text_fr': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'title_en': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'})
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
    }

    complete_apps = ['blogengine']