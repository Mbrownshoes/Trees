from django.conf.urls import patterns, url
from treemap import views


urlpatterns =patterns('',
    url(r'^$','treemap.views.map_page', name='map'), #index should be change back to map_page
    url(r'^city_trees.(?P<trees_id>\d+)/$', views.detail, name='detail'),
    url(r'^dash$','treemap.views.view_dash', name='map')
    # url(r'^/edit_feature/trees/' + r'(1060382)$','treemap.views.edit_feature'),
    ) # passed /editor/edit/N to the edit_feature() view function. 