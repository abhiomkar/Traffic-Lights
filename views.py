from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from shorturl.models import *

import urlparse

# NSFW Homepage
# -------------

def hello(request):
    return HttpResponse("Hello World!")

def homepage(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("homepage.html", c)

def post(request):
    #long_url = request.POST.get('nsfw_url', '')
    #domain = "http://" + request.META.get('HTTP_HOST', 'nsfw.in/') + "/"

    #_url = URL()
    #short_url = _url.saveURL(long_url)
    
    #response = "<tr>                                         \
                  #<td class='tleft'><a href='%s'>%s</a></td> \
                  #<td class='tright'>%s</td>                 \
                #</tr>" % (long_url, long_url, domain+short_url)

    #return HttpResponse(response, mimetype='text/html')
    pass
    return HttpResponse("nill")

