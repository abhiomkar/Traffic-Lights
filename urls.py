from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.homepage', name='home'),
    url(r'^\-post/?$', 'views.post'),
    # url(r'^(?P<shorturl_code>[a-zA-Z0-9]+)$', 'views.show_longurl'),
    # url(r'^nsfw/', include('nsfw.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls.static import static
from django.views.static import serve
urlpatterns += patterns('',
                (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT }),
               )

    # urlpatterns += staticfiles_urlpatterns()
    
    # urlpatterns += patterns('', url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': 'static/', # settings.STATIC_ROOT, }),)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
