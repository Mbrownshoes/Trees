import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 't.settings')

from django.contrib.gis.geos import fromstr
from models import Harbord

import csv
from pygeocoder import Geocoder
from django.contrib.gis.geos import (Point, fromstr, fromfile, 
                GEOSGeometry, MultiPoint, MultiPolygon, Polygon)


tree_csv = os.path.abspath('../harbordvillage/Inventory2009_test.csv')

    #Setup
with open(tree_csv, "rU") as csvinput:
    with open("../harbordvillage/outfile.csv","w") as csvoutput:
        writer = csv.writer(csvoutput,quoting=csv.QUOTE_NONNUMERIC)
    reader = csv.reader(csvinput)

    row = next(reader)
    row.append('Address')

    for row in reader:
        add=("%s %s %s %s" % (row[1], row[0], 'Toronto', 'Canada'))

        # pygeocode stuff
        # time.sleep(1)
        results = Geocoder.geocode(add)
        # print(isinstance(results, basestring))
        try:
            row.append(results[0].coordinates)
        except:
            pass

        latlong = row[5]   
        # lat = latlong[0]
        # lon = latlong[1]

        point = fromstr("POINT(%s %s)" % (latlong[0], latlong[1]))
        print(point)


        tree_obj = Harbord(Street=row[0],HouseNumber=row[1],CommonSpeciesNames=row[2],Circumference=row[3], DBH=row[4], point=point)

        tree_obj.save()

     