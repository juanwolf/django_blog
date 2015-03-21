from modeltranslation.translator import translator, TranslationOptions
from blogengine.models import Post, Category, Tag


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'slug', 'keywords')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'slug')


class TagTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'slug')

translator.register(Post, PostTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Tag, TagTranslationOptions)
