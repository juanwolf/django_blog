# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.name_en'
        db.add_column('blogengine_category', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.name_fr'
        db.add_column('blogengine_category', 'name_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.description_en'
        db.add_column('blogengine_category', 'description_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.description_fr'
        db.add_column('blogengine_category', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.slug_en'
        db.add_column('blogengine_category', 'slug_en',
                      self.gf('django.db.models.fields.SlugField')(max_length=40, null=True, unique=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.slug_fr'
        db.add_column('blogengine_category', 'slug_fr',
                      self.gf('django.db.models.fields.SlugField')(max_length=40, null=True, unique=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.name_en'
        db.add_column('blogengine_tag', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.name_fr'
        db.add_column('blogengine_tag', 'name_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.description_en'
        db.add_column('blogengine_tag', 'description_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.description_fr'
        db.add_column('blogengine_tag', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.slug_en'
        db.add_column('blogengine_tag', 'slug_en',
                      self.gf('django.db.models.fields.SlugField')(max_length=40, null=True, unique=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.slug_fr'
        db.add_column('blogengine_tag', 'slug_fr',
                      self.gf('django.db.models.fields.SlugField')(max_length=40, null=True, unique=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.name_en'
        db.delete_column('blogengine_category', 'name_en')

        # Deleting field 'Category.name_fr'
        db.delete_column('blogengine_category', 'name_fr')

        # Deleting field 'Category.description_en'
        db.delete_column('blogengine_category', 'description_en')

        # Deleting field 'Category.description_fr'
        db.delete_column('blogengine_category', 'description_fr')

        # Deleting field 'Category.slug_en'
        db.delete_column('blogengine_category', 'slug_en')

        # Deleting field 'Category.slug_fr'
        db.delete_column('blogengine_category', 'slug_fr')

        # Deleting field 'Tag.name_en'
        db.delete_column('blogengine_tag', 'name_en')

        # Deleting field 'Tag.name_fr'
        db.delete_column('blogengine_tag', 'name_fr')

        # Deleting field 'Tag.description_en'
        db.delete_column('blogengine_tag', 'description_en')

        # Deleting field 'Tag.description_fr'
        db.delete_column('blogengine_tag', 'description_fr')

        # Deleting field 'Tag.slug_en'
        db.delete_column('blogengine_tag', 'slug_en')

        # Deleting field 'Tag.slug_fr'
        db.delete_column('blogengine_tag', 'slug_fr')


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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'null': 'True', 'unique': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'null': 'True', 'unique': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'null': 'True', 'unique': 'True', 'blank': 'True'})
        },
        'blogengine.post': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Post'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['blogengine.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'unique': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'null': 'True', 'unique': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'null': 'True', 'unique': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['blogengine.Tag']"}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'default': "''"}),
            'text_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True', 'default': "''"}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True', 'default': "''"})
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'null': 'True', 'unique': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'null': 'True', 'unique': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'null': 'True', 'unique': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['blogengine']