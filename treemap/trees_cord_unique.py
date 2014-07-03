# Take trees with the same address and slightly randonmized their coordinates so they appear as seperate points on a map
from django.contrib.gis.geos import Point, MultiPoint
import random, decimal
from django.db.models import Count
from models import Trees
import re

dupes = Trees.objects.values('geom').annotate(Count('id')).order_by().filter(id__count__gt=1)

for x in dupes:
    ind =Trees.objects.filter(geom__contains=x['geom'])
    # print([p.point[0] for p in Harbord.objects.filter(point__contains=x['point'])]) 

    # test = []
    for i in ind:
        pnt = i.geom
        x=pnt.ewkt
        match = re.search('([\d.-]+) ([\d.]+)',x)
        lon =float(match.group(1))
        lon= random.uniform(lon,lon+0.0001)
        lat =float(match.group(2))
        lat= random.uniform(lat,lat+0.0001)
        xx=Point(lon,lat)
        mp=MultiPoint(xx)
        i.geom=mp
        # y[0]= random.uniform(y[0],y[0]+0.0001)
        # i.point[1] =y[1]
        # i.point[0] =y[0]
        # # test.append(i)
        i.save()


# print([p for p in dupes[1]])


# random.uniform(pt,pt+0.000001)

# 5 deciamls for 1.1m