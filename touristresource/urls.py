from django.contrib import admin
from django.urls import path, include

from touristresource.views import ListViewTouristResource, AddTouristResource, UpdateTouristResource, DetailsTouristResource, removeTouristResource 



urlpatterns = [
    path('',ListViewTouristResource.as_view(), name='listTouristResource'),
    path('add',AddTouristResource.as_view(), name='addTouristResource'),
    path('update/<resource_id>',UpdateTouristResource.as_view(),name='updateTouristResource'),
    path('detail/<resource_id>',DetailsTouristResource.as_view(),name='detailTouristResource'),
    path('remove/<resource_id>',removeTouristResource,name='removeTouristResource'),    
]