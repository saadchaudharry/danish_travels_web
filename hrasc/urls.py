"""hrasc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from cont_us.views import index,AllService,cont,Clients,about,license_s


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('service',AllService,name="service"),
    path('contact_us/', cont.as_view(),name='cont'),
    path('Client/', Clients,name='client'),
    path('licenses/', license_s,name='licenses'),
    path('about/', about,name='about'),

]


urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)