from django.urls import path
from .views import test_view, download_cv_view

app_name = "core"
urlpatterns = [
    path("", test_view, name="test"),
    path("download-cv/", download_cv_view, name="download_cv"),
]
