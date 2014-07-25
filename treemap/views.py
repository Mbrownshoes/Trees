from django.shortcuts import redirect, render,get_object_or_404
from pygeocoder import Geocoder
from django.template import RequestContext
from django.forms.widgets import HiddenInput
from django.http import HttpResponseNotFound
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from treemap import utils
from treemap.models import Trees, Harbord

def map_page(request):
     return render(request,'treemap/map.html') 

def editor(request):
    return render(request,'treemap/editor.html', {'form': TreesForm})

class IndexView(generic.ListView):
    template_name ='treemap/index.html'
    context_object_name= 'fernwood_trees'

    def get_queryset(self):
        """Return trees on Fernwood Park Ave"""
        return Trees.objects.filter(address_fu__contains="Fernwood")
# def detail(request, trees_id):
#     try:
#         tree = Trees.objects.get(pk=trees_id)
#     except Trees.DoesNotExist:
#         raise Http404
#     return render(request, 'treemap/detail.html', {'tree': tree})

def detail(request, trees_id):

    try:
        tree = Trees.objects.get(id=trees_id)
    except Tree.DoesNotExist:
        return HttpResponseNotFound()        
    

    geometry_field = 'geom'
    model_id = 'Trees'
    form_class = utils.get_map_form(model_id)

    if request.method == "GET":
        wkt = getattr(tree, geometry_field)
        form = form_class({'geometry' : wkt})

        return render(request, "treemap/detail.html",
                        {'form'          : form,
                        'tree' : tree})

    elif request.method == "POST":
        form = form_class(request.POST)
        try:
            if form.is_valid():
                wkt = form.cleaned_data['geometry']
                setattr(tree, geometry_field, wkt)
                tree.save()
                return render(request, "treemap/detail.html",
                        {'Trees'    : Trees,
                        'form'          : form})

        except ValueError:
            pass

            return render(request, "treemap/detail.html",
            {'Trees'    : Trees,
            'form'          : form,
            'attributes'    : attributes})  


# class DetailView(generic.DetailView):
#     model = Trees
#     template_name = 'treemap/detail.html'
