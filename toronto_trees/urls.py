from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'toronto_trees.views.home', name='home'),
    url(r'', include('treemap.urls', namespace='treemap')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')), 
    url(r'', include('django_browserid.urls')),
    url(r'^editor', include('treemap.urls')),

)
# urlpatterns += staticfiles_urlpatterns()