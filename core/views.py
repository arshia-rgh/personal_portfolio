import os.path

from django import views
from django.http import FileResponse
from django.shortcuts import render


def test_view(request):
    return render(request, "core/index.html")


class DownloadCView(views.View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join(os.getcwd(), "files/resume.pdf")
        return FileResponse(
            open(file_path, "rb"), as_attachment=True, filename="resume.pdf"
        )


download_cv_view = DownloadCView.as_view()
