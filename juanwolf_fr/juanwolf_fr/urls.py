from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from rest_framework_swagger.views import get_swagger_view


admin.autodiscover()

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    # Summernote
    url(r'^summernote/', include('django_summernote.urls')),

    # Internationalization
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # API
    url(r'^api/docs/', schema_view),
    url(r'^api/', include('api.urls')),
    # Blog
    url(r'', include('blogengine.urls', namespace="blog")),
]

handler404 = 'blogengine.views.page_not_found_view'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
