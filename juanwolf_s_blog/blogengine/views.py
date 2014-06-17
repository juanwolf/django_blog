from django.contrib.syndication.views import Feed
from django.shortcuts import render_to_response, render, get_object_or_404
from django.views.generic import ListView, View, TemplateView
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
            category = get_object_or_404(Category, slug=slug)
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
            tag = get_object_or_404(Tag, slug=slug)
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
        post = get_object_or_404(Post, slug=slug)
        return post

    def get_context_data(self):
        # Call the base implementation first to get a context
        # Add in a querySet the category
        context = self.get_context_categories()
        posts = Post.objects.order_by('-pub_date')
        post = self.get_queryset()
        i = 0
        while not(posts[i] == post) :
            i += 1
        context['has_next_post'] = i > 0
        if context['has_next_post'] :
            context['next_post'] = posts[i - 1]

        context['has_previous_post'] = (i + 1) < len(posts)
        if context['has_previous_post'] :
            context['previous_post'] = posts[i + 1]
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


class PageNotFoundView(IndexView):
    template_name = 'blogengine/page_not_found.html'

    def get_queryset(self):
        Post.objects.none

    def get_context_data(self):
        context = self.get_context_categories()
        return context