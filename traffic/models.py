# from django.db import models
from django.contrib.gis.db import models
import random, sys

from django.contrib.gis.geos import *
from django.contrib.gis.measure import D

# TODO
# 
#

class Setting(models.Model):
    something1 = models.IntegerField(max_length=5)
    something2 = models.IntegerField(max_length=10)

class Checkin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    checkin_time = models.DateTimeField(auto_now_add=True)
    street_addr = models.CharField(max_length=9999, default="")
    status_update = models.CharField(max_length=9999, default="")
    traffic_dense_level = models.IntegerField(max_length=5, default=0)
    plus_ones = models.IntegerField(max_length=9999, default=0)
    point = models.PointField(srid=24370)
    objects = models.GeoManager()

    def checkins_nearby_you(self, lat, lgt):
        # Checkin.objects.filter()
        # Checkin.objects.filter(point__distance_lte=(pnt, D(km=6)))
        pnt = fromstr('POINT(%s %s)' % (lat, lgt), srid=24370)

        qs = Checkin.objects.filter(point__distance_lt=(pnt, D(km=10))).order_by('point')[0:6]
        #res = '{'
        #for i, q in enumerate(qs):
            #ll = '%s,%s' % (q.latitude, q.longitude)
            #res += "latlgt%s: " % i + "'%s'" % ll
            #res += ", "

        #if res.endswith(", "):
            #res = res[:-2]

        #res += "}"

        res = '['
        for i, q in enumerate(qs):
            ll = '%s,%s' % (q.latitude, q.longitude)
            street_addr = q.street_addr
            tr_dense = q.traffic_dense_level 
            checkin_time = q.checkin_time 
            res += "{latlng: '%s', street_addr: '%s', tr_dense: %s, checkin_time: '%s'}" % (ll, street_addr, tr_dense, checkin_time)
            res += ", "

        if res.endswith(", "):
            res = res[:-2]

        res += "]"
        return res

    def do_checkin(self, lat, lgt, st_addr, tdc):
        """ Do checkin for the user
            : latitude
            : longitude
            : Street Address
            : Traffic Dense Level
        """
        from django.contrib.gis.geos import Point
        pnt = fromstr('POINT(%s %s)' % (lat, lgt), srid=24370)

        try:
            _checkin = Checkin(latitude = lat, longitude = lgt, street_addr = st_addr, traffic_dense_level = tdc, point = pnt)
        except:
            print "error: ", sys.exc_info()

        try:
            _checkin.save()
        except:
            print "error: ", sys.exc_info()
        return 

