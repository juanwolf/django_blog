from django.contrib.syndication.views import Feed

from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import translation
from django.utils.translation import ugettext as _
from django.views.generic import DetailView, ListView, RedirectView

from blogengine import models


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
                self.category = models.Category.objects.get(slug_en=slug)
                translation.activate("en")
                self.translation = 'en'
            except models.Category.DoesNotExist:
                pass
            else:
                return self.category.post_set.all().prefetch_related('tags').select_related('category')

            try:
                # Try to get the the category if not raise an exception
                self.category = models.Category.objects.get(slug_fr=slug)
                translation.activate("fr")
                self.translation = 'fr'
            except models.Category.DoesNotExist:
                raise Http404
            else:
                return models.Post.objects.filter(category__slug_fr=slug).prefetch_related('tags').select_related('category')
        else:
            translation.activate(self.translation)
            return models.Post.objects.filter(category__slug=slug).prefetch_related('tags').select_related('category')

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
            context['category'] = models.Category.objects.get(slug=slug)
        return context


class CategoryListView(ListView):
    template_name = "blogengine/category_list.html"
    context_object_name = "category_list"

    def get_queryset(self):
        return models.Category.objects.all().prefetch_related('post_set')


class TagDetailView(ListView):
    template_name = "blogengine/tag_detail.html"
    model = models.Tag
    translation = None

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = models.Tag.objects.get(slug_fr=slug)
        except models.Tag.DoesNotExist:
            pass
        else:
            posts = tag.post_set.all()
        try:
            tag = models.Tag.objects.get(slug_en=slug)
        except models.Tag.DoesNotExist:
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
            context['tag'] = models.Tag.objects.get(slug_fr=slug)
            translation.activate('fr')
            return context
        except models.Tag.DoesNotExist:
            pass
        try:
            context['tag'] = models.Tag.objects.get(slug_en=slug)
            translation.activate('en')
            return context
        except models.Tag.DoesNotExist:
            raise Http404


class PostListView(ListView):
    template_name = "blogengine/post_list.html"
    context_object_name = "post_list"

    def get_queryset(self):
        return models.Post.objects.all().select_related('category').prefetch_related('tags')


class PostDetailView(DetailView):
    template_name = "blogengine/post_detail.html"
    context_object_name = "post"
    # form_class = CommentsForm

    def get_queryset(self):
        slug = self.kwargs['slug']
        post = models.Post.objects.filter(slug_en=slug).select_related('category').prefetch_related('tags')
        if post.exists():
            translation.activate("en")
            return post
        post = models.Post.objects.filter(slug_fr=slug)
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
        except models.Post.DoesNotExist:
            context['has_next_post'] = False

        try:
            previous_post = post.get_previous_by_pub_date()
            context['has_previous_post'] = True
            context['previous_post'] = previous_post
        except models.Post.DoesNotExist:
            context['has_previous_post'] = False

        return context


class RedirectPostDetailView(RedirectView):
    permanent = True
    query_string = False
    pattern_name = 'post-detail'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(models.Post, slug=kwargs['slug'])
        kwargs['category__slug'] = post.category.slug
        return reverse_lazy('post-detail', args=[post.category.slug, kwargs['slug']])


class PostsFeed(Feed):
    title = _("RSS feed - posts")
    link = "feeds/posts/"
    description = _("RSS feed - blog posts")

    def items(self):
        return models.Post.objects.order_by('-pub_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text


def page_not_found_view(request, template_name='blogengine/page_not_found.html'):
    context = RequestContext(request)
    context['categories'] = models.Category.objects.all()
    return render_to_response(template_name, context)
