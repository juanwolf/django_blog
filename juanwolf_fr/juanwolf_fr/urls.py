from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from juanwolf_fr import views

admin.autodiscover()

urlpatterns = [
    # Internationalization
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # API
    url(r'^api/docs/', include('rest_framework_swagger.urls')),
    url(r'^api/', include('api.urls')),
    # Blog
    url(r'^blog/', include('blogengine.urls')),
    # Index
    url(r'^$', views.Index.as_view(), name="index")
]

handler404 = 'blogengine.views.page_not_found_view'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
