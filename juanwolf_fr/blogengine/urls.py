from django.conf.urls import include, url
from django.contrib.sitemaps.views import sitemap

from blogengine import views, models

sitemaps = {
    'blog': models.BlogSitemap
}

urlpatterns = [
    # Internationalization
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # Post RSS feed
    url(r'^feeds/posts/$', views.PostsFeed()),

    # Summernote
    url(r'^summernote/', include('django_summernote.urls')),

    url(
        r'^sitemap\.xml$',
        sitemap,
        {
            'sitemaps': sitemaps,
            'template_name': 'blogengine/custom_sitemap.html'
        },
        name='django.contrib.sitemaps.views.sitemap',
    ),

    # Index
    url(
        r'^(?P<page>\d+)?/?$', views.PostListView.as_view(model=models.Post, paginate_by=5)
    ),
    # Tags
    url(
        r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$',
        views.TagDetailView.as_view(model=models.Tag)
    ),
    # Individual posts
    url(
        r'^(?P<category__slug>[a-zA-Z0-9\-]+)/(?P<slug>[a-zA-Z0-9-]+)/?$',
        views.PostDetailView.as_view(model=models.Post),
        name='post-detail'
    ),
    url(
        r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$',
        views.RedirectPostDetailView.as_view()
    ),
    # Categories
    url(
        r'^(?P<slug>[a-zA-Z0-9-]+)/?$',
        views.CategoryDetailView.as_view(paginate_by=5, model=models.Category)
    ),
]



