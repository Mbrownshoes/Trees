from django.contrib.gis import forms
from treemap.models import Trees
# from django.views.generic import UpdateView


class TreesForm(forms.ModelForm):

    class Meta:
        model = Trees
        fields = ('common_nam','geom')
        widgets = {
        'geom': LeafletWidget()
        }

class EditTrees(UpdateView):
    model = Trees
    form_class = TreesForm
    template_name = 'forms.html'


