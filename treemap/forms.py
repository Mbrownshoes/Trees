from django.contrib.gis import forms
from treemap.models import Trees
from django.contrib.gis import admin

# from django.views.generic import UpdateView



import floppyforms as forms

class MultiPointWidget(forms.gis.MultiPointWidget, forms.gis.BaseOsmWidget):
    map_template = "treemap/osm.html"

class MapForm(forms.ModelForm):
    class Meta:
        model = Trees
        widgets = {
            'geom': MultiPointWidget,
        }
  
    feature = forms.gis.MultiPointField(widget=MultiPointWidget)
# class EditTrees(UpdateView):
#     model = Trees
#     form_class = TreesForm
#     template_name = 'forms.html'


class CustomGeoModelAdmin(admin.OSMGeoAdmin):
    form = MapForm
        # map_template = "treemap/osm.html"

# admin_instance=CustomGeoModelAdmin(Trees, admin.site)
# field = Trees._meta.get_field('geom')
# widget_type = admin_instance.get_map_widget(field)
# wkt = getattr(tree, geometry_field)
# form = form_class({'geometry' : wkt})