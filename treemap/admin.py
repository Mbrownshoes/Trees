from django.contrib.gis import admin
from models import Trees
# Register your models here.

admin.site.register(Trees, admin.OSMGeoAdmin)
