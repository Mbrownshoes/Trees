from django.shortcuts import render_to_response
from pygeocoder import Geocoder


from models import Trees, Harbord
# from django.views.generic import TemplateView
# Create your views here.

# class MapView(TemplateView):
#     template_name="treemap/index.html"

#  old way - workes!
# def index(request):
#     # 'Display Map'
#     treepoints = Trees.objects.all().order_by('common_nam')
#     return render_to_kml('treemap/placemarks.kml', {
#         'treepoints' : treepoints})


# def index(request):
#     # 'Display Map'
#     treepoints = Trees.objects.kml()
#     return render_to_kml('gis/kml/placemark2.kml', {
#         'places' : treepoints})

def map_page(request):
     lcount = Trees.objects.all().count()
     return render_to_response('treemap/map.html', {'tree_count' : lcount}) 

