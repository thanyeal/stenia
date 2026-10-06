from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("files/", views.files_browser, name="files_browser"),
    path("my-files/", views.my_files, name="my_files"),
    path("shared/", views.shared_with_me, name="shared_with_me"),
    path("recent/", views.recent, name="recent"),
    path("trash/", views.recently_deleted, name="recently_deleted"),
    path("settings/", views.settings, name="settings"),
    path("integrations/", views.integrations, name="integrations"),
    path("profile/", views.profile, name="profile"),
    path("setup/telegram/", views.telegram_setup, name="telegram_setup"),
]