from django.contrib import admin
from django.contrib.admin import ModelAdmin
from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin

from blogengine.models import Post, Category, Tag


class PostAdmin(TranslationAdmin, SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",),
                           "slug_en": ("title_en",),
                           "slug_fr": ("title_fr",)}


class CategoryAdmin(TranslationAdmin, ModelAdmin):
    prepopulated_fields = {"slug": ("name",),
                           "slug_en": ("name_en",),
                           "slug_fr": ("name_fr",)}


class TagAdmin(TranslationAdmin, ModelAdmin):
    prepopulated_fields = {"slug": ("name",),
                           "slug_en": ("name_en",),
                           "slug_fr": ("name_fr",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)