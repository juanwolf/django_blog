from modeltranslation.translator import register, TranslationOptions

from blogengine.models import Post, Category, Tag


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'slug', 'keywords')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'slug')


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'slug')

