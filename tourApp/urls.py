"""
URL configuration for tourApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from tour import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search_result', views.home, name='search_result'),
    path('mombasa', views.mombasa, name='mombasa'),
    path('diani', views.diani, name='diani'),
    path('watamu', views.watamu, name='watamu'),
    path('shimoni', views.shimoni, name='shimoni'),
    path('mambrui', views.mambrui, name='mambrui'),
    path('wasini', views.wasini, name='wasini'),
    path('listings', views.hotels, name='hotels'),
    path('listings', views.restaurants, name='restaurants'),
    path('listings', views.destinations, name='destinations'),
    path('listings', views.travels, name='travels'),   
    path('register', views.register, name='register'),
     path('unregister', views.unregister, name='unregister')
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
