"""annotate URL Configuration

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
from app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='Home Page'),
    url(r'^login/',views.user_login, name='Login'),
    url(r'^register/',views.user_register, name='Register'),
    url(r'^home/',views.home, name='Home for logged in'),
    url(r'^logout/',views.logout_user, name='Logout'),
    url(r'^add/',views.add_code,name='Add Code'),
    url(r'^code/(?P<codeid>\d+)/$', views.view_code, name="View Code"),
    url(r'^api/add_ann/$', views.add_annotation, name="Add Annotation"),
    url(r'^delete_code/(?P<codeid>\d+)/$', views.delete_code, name="Delete Code")

]

