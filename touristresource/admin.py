from django.contrib import admin
from touristresource.models import TouristResourceImage,TouristResource
# Register your models here.

class TouristResourceAdmin(admin.ModelAdmin):
    pass

class TouristResourceImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(TouristResourceImage,TouristResourceImageAdmin)
admin.site.register(TouristResource,TouristResourceAdmin)