import random, decimal
from django.db.models import Count
from models import Harbord


dupes = Harbord.objects.values('point').annotate(Count('id')).order_by().filter(id__count__gt=1)

for x in dupes:
    ind =Harbord.objects.filter(point__contains=x['point'])
    # print([p.point[0] for p in Harbord.objects.filter(point__contains=x['point'])]) 

    # test = []
    for i in ind:
        pnt = i.point
        y=([coord for coord in pnt])
        y[1]= random.uniform(y[1],y[1]+0.0001)
        y[0]= random.uniform(y[0],y[0]+0.0001)
        i.point[1] =y[1]
        i.point[0] =y[0]
        # test.append(i)
        i.save()


# print([p for p in dupes[1]])


# random.uniform(pt,pt+0.000001)

# 5 deciamls for 1.1m