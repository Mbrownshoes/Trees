# Used this to load up harbord trees.
# First I did this:
# Remove your migrations directory: rm -Rf your_app/migrations/
# Sync and migrate in just one command: python manage.py syncdb --migrate 

# Then:
# python manage.py shell
# from treemap import load_up

import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 't.settings')

from django.contrib.gis.geos import fromstr
from models import Harbord
import time
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
        time.sleep(0.25)
        results = Geocoder.geocode(add)
        # print(isinstance(results, basestring))
        try:
            row.append(results[0].coordinates)
        except:
            pass
        #add street suffix to street    
        row[0] = results.route
        # print(row)
        latlong = row[5]   


        point = fromstr("POINT(%s %s)" % (latlong[1], latlong[0]))
        # print(point)

        tree_obj = Harbord(Street=row[0],HouseNumber=row[1],CommonSpeciesNames=row[2],Circumference=row[3], DBH=row[4], point=point)

        tree_obj.save()

     