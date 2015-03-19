from django.contrib import admin
from django.contrib.admin import ModelAdmin
from blogengine.models import Post, Category, Tag
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",),
                           "slug_en": ("title_en",),
                           "slug_fr": ("title_fr",)}


class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",),
                           "slug_en": ("name_en",),
                           "slug_fr": ("name_fr",)}


class TagAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",),
                           "slug_en": ("name_en",),
                           "slug_fr": ("name_fr",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)