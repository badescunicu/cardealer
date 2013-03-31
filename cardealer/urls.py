from django.conf.urls import patterns, include, url
from django.conf import settings
from cardealer.views import ListCars

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cardealer.views.home', name='home'),
#    url(r'^cars/$', 'cardealer.views.list_all_cars', name='list_all_cars'),
    url(r'^cars/$', ListCars.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include('api.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^resources/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
