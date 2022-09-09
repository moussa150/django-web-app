from django.contrib import admin

from listings.models import Band

from listings.models import Annonce

# Register your models here.

class BandAdmin(admin.ModelAdmin):
    list_display=('name','year_formed','genre')

class AnnonceAdmin(admin.ModelAdmin):
    list_display=('titre','description','sold','year','type','band')

admin.site.register(Band,BandAdmin)
admin.site.register(Annonce,AnnonceAdmin)