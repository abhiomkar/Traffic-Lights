from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from traffic.models import *

import urlparse

# NSFW Homepage
# -------------

def hello(request):
    return HttpResponse("Hello World!")

def homepage(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("homepage.html", c)

def checkins_nearby_you(request):
    return render_to_response("checkins.html")

def getcheckins(request):
    latitude = request.GET.get('latitude', '')
    longitude = request.GET.get('longitude', '')
    _checkin = Checkin()
    response = _checkin.checkins_nearby_you(latitude, longitude)
    return HttpResponse(response)

def post(request):
    latitude = request.POST.get('latitude', '')
    longitude = request.POST.get('longitude', '')
    street_address = request.POST.get('street_address', '')
    traffic_dense_level = request.POST.get('traffic_dense_level', '')
    latlng = request.POST.get('latlng', '')
    print('lat: %s' % latitude)
    print('lng: %s' % longitude)
    print('street_address: %s' % street_address)
    print('traffic_dense_level: %s' % traffic_dense_level)

    #domain = "http://" + request.META.get('HTTP_HOST', 'trlights.com/') + "/"

    _checkin = Checkin()
    _checkin.do_checkin(latitude, longitude, street_address, traffic_dense_level)

    
    response = "Checked in at " + street_address
    return HttpResponse(response, mimetype='text/html')
    
    #response = "<tr>                                         \
                  #<td class='tleft'><a href='%s'>%s</a></td> \
                  #<td class='tright'>%s</td>                 \
                #</tr>" % (long_url, long_url, domain+short_url)

    #return HttpResponse(response, mimetype='text/html')

