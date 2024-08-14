from django.shortcuts import render
from django import views


def test_view(request):
    return render(request, "core/index.html")


class DownloadCView(views.View):
    def get(self, request, *args, **kwargs):
        pass
