from django.contrib.syndication.views import Feed
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import translation
from django.utils.translation import ugettext as _
from django.views.generic import DetailView, ListView

from blogengine.models import Category, Post, Tag


class CategoryDetailView(ListView, DetailView):
    template_name = "blogengine/category_detail.html"
    context_object_name = "post_list"
    translation = None
    category = None

    def get_queryset(self):
        slug = self.kwargs['slug']
        if not self.translation:
            try:
                # Try to get the category if not raise an exception
                self.category = Category.objects.get(slug_en=slug)
                translation.activate("en")
                self.translation = 'en'
            except Category.DoesNotExist:
                pass
            else:
                return self.category.post_set.all().prefetch_related('tags').select_related('category')

            try:
                # Try to get the the category if not raise an exception
                self.category = Category.objects.get(slug_fr=slug)
                translation.activate("fr")
                self.translation = 'fr'
            except ObjectDoesNotExist:
                raise Http404
            else:
                return Post.objects.filter(category__slug_fr=slug).prefetch_related('tags').select_related('category')
        else:
            translation.activate(self.translation)
            return Post.objects.filter(category__slug=slug).prefetch_related('tags').select_related('category')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        # Add in a querySet the category
        self.object = self.get_queryset()
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        translation.activate(self.translation)
        if self.category:
            context['category'] = self.category
        else:
            context['category'] = Category.objects.get(slug=slug)
        return context


class CategoryListView(ListView):
    template_name = "blogengine/category_list.html"
    context_object_name = "category_list"

    def get_queryset(self):
        return Category.objects.all().prefetch_related('post_set')


class TagDetailView(ListView):
    template_name = "blogengine/tag_detail.html"
    model = Tag
    translation = None

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = Tag.objects.get(slug_fr=slug)
        except Tag.DoesNotExist:
            pass
        else:
            posts = tag.post_set.all()
        try:
            tag = Tag.objects.get(slug_en=slug)
        except ObjectDoesNotExist:
            raise Http404
        else:
            posts = tag.post_set.all()

        return tag.post_set.all().select_related('category').prefetch_related('tags')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        # Add in a querySet the category
        context = super(TagDetailView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        try:
            context['tag'] = Tag.objects.get(slug_fr=slug)
            translation.activate('fr')
            return context
        except ObjectDoesNotExist:
            pass
        try:
            context['tag'] = Tag.objects.get(slug_en=slug)
            translation.activate('en')
            return context
        except ObjectDoesNotExist:
            raise Http404


class PostListView(ListView):
    template_name = "blogengine/post_list.html"
    context_object_name = "post_list"

    def get_queryset(self):
        return Post.objects.all().select_related('category').prefetch_related('tags')


class PostDetailView(DetailView):
    template_name = "blogengine/post_detail.html"
    context_object_name = "post"
    # form_class = CommentsForm

    def get_queryset(self):
        slug = self.kwargs['slug']
        post = Post.objects.filter(slug_en=slug).select_related('category').prefetch_related('tags')
        if post.exists():
            translation.activate("en")
            return post
        post = Post.objects.filter(slug_fr=slug)
        if post.exists():
            translation.activate("fr")
            return post.prefetch_related('tags').select_related('category').prefetch_related('tags')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        # Add in a querySet the category
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = context['post']

        try:
            next_post = post.get_next_by_pub_date()
            context['next_post'] = next_post
            context['has_next_post'] = True
        except Post.DoesNotExist:
            context['has_next_post'] = False

        try:
            previous_post = post.get_previous_by_pub_date()
            context['has_previous_post'] = True
            context['previous_post'] = previous_post
        except Post.DoesNotExist:
            context['has_previous_post'] = False

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


def page_not_found_view(request, template_name='blogengine/page_not_found.html'):
    context = RequestContext(request)
    context['categories'] = Category.objects.all()
    return render_to_response(template_name, context)
