"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from application.views import LoginView, HomeView, ContactView, ProfileView, ReportView, FAQView, logoutView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.conf import settings


import accescontrol.urls
import touristresource.urls
import api.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginView.as_view(), name='index'),
    path('home',HomeView.as_view(), name='home'),
    path('contact',ContactView.as_view(), name='contact'),
    path('profile',ProfileView.as_view(), name='profile'),
    path('logout',logoutView, name='logout'),
    path('report',ReportView.as_view(), name='report'),
    path('faq',FAQView.as_view(), name='faq'),

    path('accescontrol/',include(accescontrol.urls)),
    path('touristresource/',include(touristresource.urls)),
    
    path('api/',include(api.urls)),
    
]

urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
