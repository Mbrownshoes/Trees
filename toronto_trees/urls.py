from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import patterns, include, url
from django.contrib.gis import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'toronto_trees.views.home', name='home'),
    url(r'^$', 'treemap.views.map_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')), 
    url(r'', include('django_browserid.urls')),

)
# urlpatterns += staticfiles_urlpatterns()