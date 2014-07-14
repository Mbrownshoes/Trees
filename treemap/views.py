from django.shortcuts import redirect, render
from pygeocoder import Geocoder
from django.template import RequestContext
from django.forms.widgets import HiddenInput

# from treemap.forms import UserForm, UserProfileForm

from treemap.models import Trees, Harbord

def map_page(request):
     lcount = Trees.objects.all().count()
     return render(request,'treemap/map.html', {'tree_count' : lcount}) 

