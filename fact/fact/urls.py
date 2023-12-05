from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", include("fact.portfolio.urls"), name="portfolio"),
    path("admin/", admin.site.urls)
]