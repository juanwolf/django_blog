from django.conf.urls import include, url, patterns
from blogengine.models import Post, Category, Tag, BlogSitemap
from blogengine.views import PostListView, CategoryDetailView, PostsFeed, TagDetailView, \
    PostDetailView

sitemaps = {
    'blog': BlogSitemap
}

urlpatterns = patterns('',

    # Internationalization
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # Index
    url(r'^(?P<page>\d+)?/?$', PostListView.as_view(
        model=Post,
        paginate_by=5,
        )),
    # Tags
    url(r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$', TagDetailView.as_view(
        model=Tag,
        )),
    # Individual posts
    url(r'^(?P<category__slug>[a-zA-Z0-9\-]+)/(?P<slug>[a-zA-Z0-9-]+)/?$', PostDetailView.as_view(
        model=Post,)),

    # Categories
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/?$', CategoryDetailView.as_view(
        paginate_by=5,
        model=Category,
        )),

    # Post RSS feed
    url(r'^feeds/posts/$', PostsFeed()),

    # Summernote
    url(r'^summernote/', include('django_summernote.urls')),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps,
         'template_name': 'blogengine/custom_sitemap.html'}),
)


