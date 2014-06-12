from django.contrib.syndication.views import Feed
from django.views.generic import ListView, View
from blogengine.models import Category, Post, Tag
from django.utils.translation import ugettext as _


class IndexView(ListView):
    def get_context_categories(self):
        context = super(IndexView, self).get_context_data(**self.kwargs)
        context['categories'] = Category.objects.all()
        return context



class CategoryDetailView(IndexView):
    template_name = "blogengine/category_detail.html"
    context_object_name = "post_list"

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            return Post.objects.filter(category=category)
        except Category.DoesNotExist:
            return Post.objects.none()

    def get_context_data(self):
        # Call the base implementation first to get a context
        # Add in a querySet the category
        context = self.get_context_categories()
        slug = self.kwargs['slug']
        context['category'] = Category.objects.get(slug=slug)
        return context


class CategoryListView(IndexView):
    template_name = "blogengine/category_list.html"
    context_object_name = "category_list"

    def get_queryset(self):
        return Category.objects.all()


class TagDetailView(IndexView):
    template_name = "blogengine/tag_detail.html"

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = Tag.objects.get(slug_en=slug)
            return tag.post_set.all()
        except Tag.DoesNotExist:
            return Post.objects.none()

    def get_context_data(self):
        # Call the base implementation first to get a context
        # Add in a querySet the category
        context = self.get_context_categories()
        slug = self.kwargs['slug']
        context['tag'] = Tag.objects.get(slug=slug)
        return context


class PostListView(IndexView):
    template_name = "blogengine/post_list.html"
    context_object_name = "post_list"

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self):
        # Call the base implementation first to get a context
        # Add in a querySet the category
        context = self.get_context_categories()
        return context

class PostDetailView(IndexView):
    template_name = "blogengine/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.get(slug=slug)

    def get_context_data(self):
        # Call the base implementation first to get a context
        # Add in a querySet the category
        context = self.get_context_categories()
        return context

class PostsFeed(Feed):
    title = _("RSS feed - posts")
    link = "feeds/posts/"
    description = _("RSS feed - blog posts")

    def items(self):
        return Post.objects.order_by('-pub_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text
