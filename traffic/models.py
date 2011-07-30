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

    def checkins_nearby_you(lat, lgt):
        # Checkin.objects.filter()
        # Checkin.objects.filter(point__distance_lte=(pnt, D(km=6)))
        return

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

