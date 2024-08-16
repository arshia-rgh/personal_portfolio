import os.path

from django import views
from django.http import FileResponse
from django.views.generic import TemplateView

from core.models import Skill, Project, JobExperience, Education, Interest, Certificate


class HomeView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "arshia"
        context["skills"] = Skill.objects.all()
        context["projects"] = Project.objects.all()
        context["jobs"] = JobExperience.objects.all()
        context["educations"] = Education.objects.all()
        context["interests"] = Interest.objects.all()
        context["certificates"] = Certificate.objects.all()
        return context


home_view = HomeView.as_view()


class DownloadCVView(views.View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join(os.getcwd(), "files/resume.pdf")
        return FileResponse(
            open(file_path, "rb"), as_attachment=True, filename="resume.pdf"
        )


download_cv_view = DownloadCVView.as_view()
