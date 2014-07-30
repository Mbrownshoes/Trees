from django import forms
from django.contrib.gis.geos.collections import MultiPolygon, MultiLineString

from django.contrib.gis import admin
from treemap.models import Trees


def get_map_form(model_id):
    class CustomGeoModelAdmin(admin.OSMGeoAdmin):
        map_template = "treemap/osm.html"
        
    admin_instance=CustomGeoModelAdmin(Trees, admin.site)
    field = Trees._meta.get_field('geom')
    widget_type = admin_instance.get_map_widget(field)


    class MapForm(forms.Form):
        geometry = forms.CharField(widget=widget_type(),
            label ="")

    return MapForm


