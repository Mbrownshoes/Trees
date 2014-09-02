import datetime
from django.shortcuts import redirect, render,get_object_or_404
from pygeocoder import Geocoder
from django.template import RequestContext
from django.forms.widgets import HiddenInput
from django.http import HttpResponseNotFound
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.admin.models import LogEntry
from django.shortcuts import render_to_response
from treemap import utils
from treemap.models import Trees, Harbord

from django.contrib.auth import get_user_model
User = get_user_model()

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
    except tree.DoesNotExist:
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
                        {'form'          : form,
                        'tree' : tree})

        except ValueError:
            pass

            return render(request, "treemap/detail.html",
            {'Trees'    : Trees,
            'form'          : form,
            'attributes'    : attributes})  


def view_dash(request):
    today = datetime.date.today()
    user = request.user 
    proj_perm = user.has_perm('project.add_project')
    project = Trees.objects.all().order_by('-proj_name')
    query = Trees.objects.all().order_by('-id')[:5]
    # que_quotes = Trees.objects.filter(status__value__exact = 'Quote')
    # expired = FollowUp.objects.filter(next_followup__lte=today).order_by('next_followup').filter(archived=False)
    log = LogEntry.objects.select_related().all().order_by("-id")
    hist = Trees.history.all()
    # user = User.objects.get(email)
    # print(user)
    return render_to_response('treemap/dash.html', {'user': user, 'project': project, 'query':query,
                                                      'proj_perm':proj_perm, 'log': log, 'hist':hist,}, context_instance=RequestContext(request))
