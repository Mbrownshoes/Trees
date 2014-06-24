import os
import time
# from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import fromstr
# from models import Harbord

import csv
from pygeocoder import Geocoder
# from django.contrib.gis.geos import (Point, fromstr, fromfile, 
#                 GEOSGeometry, MultiPoint, MultiPolygon, Polygon)


tree_csv = os.path.abspath('../harbordvillage/Inventory2009_test.csv')

    #Setup
with open(tree_csv, "rU") as csvinput:
    with open("../harbordvillage/outfile.csv","w+") as csvoutput:
        writer = csv.writer(csvoutput,quoting=csv.QUOTE_NONNUMERIC)
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append('Address')
        all.append(row)

        for row in reader:
            add=("%s %s %s %s" % (row[1], row[0], 'Toronto', 'Canada'))

            # pygeocode stuff
            # time.sleep(1)
            results = Geocoder.geocode(add)
            # print(isinstance(results, basestring))
            ind = results[0].coordinates
            lat=ind[0]
            lon=ind[1]
            ind= str(lat) + ' ' + str(lon)
            print(ind)
            mypoint = fromstr('POINT('+ ind + ')')
            # print(type(mypoint))
            try:
                row.append(mypoint)
            except:
                pass


            all.append(row)
            print(row)
            # row.append(results.cooridnates)
            # print(row)

        writer.writerows(all)


