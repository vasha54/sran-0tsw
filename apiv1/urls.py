from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from apiv1.views import ResourceTouristDetailApiView


urlpatterns = [
    path('resource_tourist/<pk>',ResourceTouristDetailApiView.as_view(),name='view_api_resource_tourist'),
]