from django.contrib import admin
from django.urls import path
from django.urls import include

app_name = "to_do_app"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("to-do/", include("to_do_app.urls")),
]
