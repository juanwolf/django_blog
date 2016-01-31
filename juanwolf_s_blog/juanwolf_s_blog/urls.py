from django.conf.urls import patterns, include, url
from django.contrib import admin
from juanwolf_s_blog import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'', include('blogengine.urls')),
)

handler404 = 'blogengine.views.page_not_found_view'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)),)