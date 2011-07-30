from django.contrib import admin
from shorturl.models import *

class ShortURLAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'

admin.site.register(URL, ShortURLAdmin)
admin.site.register(Setting)
