from django.contrib.gis.db import models

# Create your models here.

class Trees(models.Model):
    address_po = models.IntegerField()
    address_fu = models.CharField(max_length=131)
    objectid = models.IntegerField()
    struct_id = models.CharField(max_length=20)
    common_nam = models.CharField(max_length=254)
    botanical_field = models.CharField(max_length=254)
    diameter_b = models.IntegerField()
    tree_posit = models.IntegerField()
    geom = models.MultiPointField(srid=4326)
    objects = models.GeoManager()
    # mpoly = models.MultiPolygonField()

    def __unicode__(self):
        return self.common_nam

