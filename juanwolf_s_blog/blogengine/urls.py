from django.conf.urls import include, url, patterns
from django.views.generic import ListView, DetailView
from blogengine.models import Post, Category, Tag
from blogengine.views import CategoryDetailView, CategoryListView, PostsFeed, TagDetailView

urlpatterns = patterns('',
    # Index
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
        )),

    # Individual posts
    url(r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
        model=Post,
        )),

    # Categories
    url(r'^category/?$', CategoryListView.as_view(model=Category)),
    url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/?$', CategoryDetailView.as_view(
        paginate_by=5,
        model=Category,
        )),


    # Post RSS feed
    url(r'^feeds/posts/$', PostsFeed()),

    # Summernote
    url(r'^summernote/', include('django_summernote.urls')),

    # Tags
    url(r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$', TagDetailView.as_view(
        paginate_by=5,
        model=Tag,
        )),
    # Internationalization
    url(r'^i18n/', include('django.conf.urls.i18n')),
)
