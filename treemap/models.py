from django.contrib.gis.db import models
from django.contrib.auth.models import User


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

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
    
    class Meta:
        unique_together =('address_po','struct_id','objectid')

    def __str__(self):
        return self.common_nam


class Harbord(models.Model):
    Street = models.CharField(null=True, max_length=255)
    HouseNumber = models.CharField(null=True,max_length=255)
    CommonSpeciesNames = models.CharField(max_length=255)
    Circumference = models.CharField(max_length=255)
    DBH = models.CharField(max_length=255)
    point = models.PointField()

    objects = models.GeoManager()

    class Meta:
        unique_together=('Street','HouseNumber','CommonSpeciesNames','Circumference','DBH','point')

    def __str__(self):
        return self.CommonSpeciesNames












