from django.conf.urls import patterns, url
from treemap import views


# urlpatterns =patterns('',
#     url(r'^$',views.MapView.as_view()))

urlpatterns =patterns('',
    # url(r'^$',views.index, name='index'),
        (r'^$', views.map_page),
    )