from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import patterns, include, url
from django.contrib.gis import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'toronto_trees.views.home', name='home'),
    url(r'^treemap/', include('treemap.urls')),
        (r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()