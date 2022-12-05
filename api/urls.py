from django.urls import path

from api.views import *

urlpatterns = [
    path('v1/touristresource/post', TouristResourceAPIView.as_view()), 
    path('v1/touristresource/post/<id_resource>/', TouristResourceAPIViewDetail.as_view()),
    
]