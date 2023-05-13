"""DataVizSite URL Configuration

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
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('uploadedfile_home', views.uploadfile_home, name='uploadfile_home'),
    path('data-bar', views.databar, name='data-bar'),
    path('data-line', views.dataline, name='data-line'),
    path('data-pie', views.datapie, name='data-pie'),
    path('data-radar', views.dataradar, name='data-radar'),
    path('file-pie', views.filepie, name='file-pie'),
    path('file-bar', views.filebar, name='file-bar'),
    path('file-line', views.fileline, name='file-line'),
    path('file-radar', views.fileradar, name='file-radar'),

]

urlpatterns += staticfiles_urlpatterns()
