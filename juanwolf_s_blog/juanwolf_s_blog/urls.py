from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogengine.views import PageNotFoundView, PageNotFoundViewBis

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blogengine.urls')),
)

handler404 = PageNotFoundView.as_view()