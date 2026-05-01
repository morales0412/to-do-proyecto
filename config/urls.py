from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("to_do_app.urls")),
    path("", include("usuarios.urls")),
]
