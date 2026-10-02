from django.urls import path

from . import views

urlpatterns = [
    path("", views.files_browser, name="files_browser"),
]