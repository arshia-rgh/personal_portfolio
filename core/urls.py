from django.urls import path
from .views import home_view, download_cv_view

app_name = "core"
urlpatterns = [
    path("", home_view, name="home"),
    path("download-cv/", download_cv_view, name="download_cv"),
]
