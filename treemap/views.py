from django.shortcuts import redirect, render,get_object_or_404
from pygeocoder import Geocoder
from django.template import RequestContext
from django.forms.widgets import HiddenInput
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from django.views import generic
# from treemap.forms import TreesForm, MultiPointWidget

from treemap.models import Trees, Harbord

def map_page(request):
     lcount = Trees.objects.all().count()
     return render(request,'treemap/map.html', {'tree_count' : lcount}) 

def editor(request):
    return render(request,'treemap/editor.html', {'form': TreesForm})

class IndexView(generic.ListView):
    template_name ='treemap/index.html'
    context_object_name= 'fernwood_trees'

    def get_queryset(self):
        """Return trees on Fernwood Park Ave"""
        return Trees.objects.filter(address_fu__contains="Fernwood")

class DetailView(generic.DetailView):
    model = Trees
    template_name = 'treemap/detail.html'







