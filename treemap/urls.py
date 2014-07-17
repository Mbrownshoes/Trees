from django.conf.urls import patterns, url
from treemap import views


urlpatterns =patterns('',
    url(r'^$','treemap.views.map_page', name='map'), #index should be change back to map_page
    url(r'^city_trees.(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^/edit_feature/trees/' + r'(1060382)$','treemap.views.edit_feature'),
    ) # passed /editor/edit/N to the edit_feature() view function. 