# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('blogengine_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('blogengine', ['Category'])

        # Adding field 'Post.category'
        db.add_column('blogengine_post', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogengine.Category'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('blogengine_category')

        # Deleting field 'Post.category'
        db.delete_column('blogengine_post', 'category_id')


    models = {
        'blogengine.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'blogengine.post': {
            'Meta': {'object_name': 'Post', 'ordering': "['-pub_date']"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogengine.Category']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40', 'unique': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''"})
        }
    }

    complete_apps = ['blogengine']