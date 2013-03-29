from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = patterns('',
    url(r'^manufacturers/$', views.ManufacturerList.as_view()),
    url(r'^manufacturers/(?P<pk>\d+)/$', views.ManufacturerDetail.as_view()),
    url(r'^cars/$', views.CarList.as_view()),
    url(r'^cars/(?P<pk>\d+)/$', views.CarDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
