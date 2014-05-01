from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from pages.views import *

from django.contrib import admin
admin.autodiscover()

handler404 = 'pages.views.notfound'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', index, name='index'),
    url(r'^index/', index, name='index'),
    url(r'^$', index, name='index'),
)

urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)