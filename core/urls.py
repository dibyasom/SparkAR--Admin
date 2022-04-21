from django.contrib import admin
from django.urls import path

from core.views import sync_with_remote_server

urlpatterns = [
    path("sync", sync_with_remote_server),
]
