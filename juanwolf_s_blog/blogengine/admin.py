from django.contrib import admin
from blogengine.models import Post, Category, Tag
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",),
                           "slug_en": ("title_en",),
                           "slug_fr": ("title_fr",),}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)