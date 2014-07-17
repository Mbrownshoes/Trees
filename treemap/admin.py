from django.contrib.gis import admin
from treemap.models import Trees, Harbord
# Register your models here.

admin.site.register(Trees, admin.OSMGeoAdmin)
admin.site.register(Harbord, admin.OSMGeoAdmin )
