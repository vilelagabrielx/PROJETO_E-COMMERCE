# pylint: disable=missing-module-docstring
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    # TODO: remover debug toolbar
    path("__debug__/", include("debug_toolbar.urls")),
]
