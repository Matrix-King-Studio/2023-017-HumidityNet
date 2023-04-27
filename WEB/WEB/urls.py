"""WEB URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from rest_framework import routers

from app.views import SensorDataViewSet, chart_view

router = routers.DefaultRouter()
router.register("sensor", SensorDataViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("chart/", chart_view, name="chart"),
    path("api/rest-auth/", include("dj_rest_auth.urls")),
    path("api/rest-auth/registration/", include("dj_rest_auth.registration.urls"))
]
urlpatterns += staticfiles_urlpatterns()
