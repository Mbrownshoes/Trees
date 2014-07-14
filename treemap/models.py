from django.contrib.gis.db import models
from django.contrib.auth.models import User
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

    def __str__(self):
        return self.common_nam

# from django.db import models

class Harbord(models.Model):
    Street = models.CharField(null=True, max_length=255)
    HouseNumber = models.CharField(null=True,max_length=255)
    CommonSpeciesNames = models.CharField(max_length=255)
    Circumference = models.CharField(max_length=255)
    DBH = models.CharField(max_length=255)
    point = models.PointField()

    objects = models.GeoManager()


    def __str__(self):
        return self.CommonSpeciesNames

# class UserProfile(models.Model):
#     user = models.OneToOneField(User)

#     picture = models.ImageField(upload_to='profile_images', blank = True)

#     def __unicode__(self):
#         return self.user.username