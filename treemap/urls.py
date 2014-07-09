from django.conf.urls import patterns, url

# urlpatterns =patterns('',
#     url(r'^$',views.MapView.as_view()))

urlpatterns =patterns('',
    # url(r'^$',views.index, name='index'),
    url(r'^$', 'treemap.views.map_page'),
    )