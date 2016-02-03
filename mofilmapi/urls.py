"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from movies import views
#from quickstart imp
from rest_framework.routers import DefaultRouter
from project import views
from movies.views import MoviesViewSet
from project.views import ClientViewSet
from portal.views import PortalViewSet
from portal.views import PortalProjectViewSet
from users.views import UserViewSet
from portal.views import PortalContentViewSet
from mofilmuser.views import MofilmUserViewSet

from rest_framework.versioning import NamespaceVersioning
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


router = routers.DefaultRouter()
router.register(r'movies', MoviesViewSet)
router.register(r'project', ClientViewSet)
router.register(r'portal', PortalViewSet)
#router.register(r'portal/(?P<pk>[0-9]+)/portalProject/(?<pid>[0-9]+)', PortalViewSet)
#router.register(r'portal/(?P<portal_pk>\d+)/portalProject/(?P<portalProject_pk>\d+)', PortalViewSet, 'portalProject')
#router.register(r'portal/(?P<portal_pk>\d+)/portalProject/(?P<portalProject_pk>\d+)', PortalViewSet, 'portal-Project')
#router.register(r'portal/portalProject', PortalViewSet.as_view({ 'get' : 'portalProject'}))
router.register(r'portalProject', PortalProjectViewSet)
router.register(r'users', UserViewSet)
router.register(r'portalContent', PortalContentViewSet)
router.register(r'mofilmuser', MofilmUserViewSet)

portalProj = PortalViewSet.as_view({'get': 'portalPr'},)

urlpatterns = [
    url(r'^v1/', include(router.urls, namespace='v1'),),
    url(r'^portal/(?P<pk>[0-9]+)/portalProject/(<pid>[0-9]+)/', portalProj),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),

]

urlpatterns += staticfiles_urlpatterns()

