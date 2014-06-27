# Used this to load up harbord trees. Data were geocoded using pygeocder
# First I did this:
# Remove your migrations directory: rm -Rf your_app/migrations/
# Sync and migrate in just one command: python manage.py syncdb --migrate 

# Then:
# python manage.py shell
# from treemap import load_csv_trees

import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 't.settings')

from models import Harbord
import csv
from django.contrib.gis.geos import (Point, fromstr, fromfile, 
                GEOSGeometry, MultiPoint, MultiPolygon, Polygon)


tree_csv = os.path.abspath('../harbordvillage/outfile.csv')

    #Setup
with open(tree_csv, "rU") as csvinput:
        reader = csv.reader(csvinput)
        row = next(reader)


        for row in reader:
                latlong = row[5]  
                for ch in ['(',')']:
                    if ch in latlong:
                        latlong=latlong.replace(ch,'')
                latlong = latlong.split(',')
                # print(latlong[0])
                point = fromstr("POINT(%s %s)" % (latlong[1], latlong[0]))

                tree_obj = Harbord.objects.get_or_create(Street=row[0],HouseNumber=row[1],CommonSpeciesNames=row[2],Circumference=row[3], DBH=row[4], point=point)


     