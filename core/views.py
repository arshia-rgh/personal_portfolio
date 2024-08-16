import os.path

from django import views
from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Skill, Project, JobExperience, Education, Interest, Certificate


# def test_view(request):
#     skills = Skill.objects.all()
#     projects = Project.objects.all()
#     jobs = JobExperience.objects.all()
#     educations = Education.objects.all()
#     interests = Interest.objects.all()
#     certificates = Certificate.objects.all()
#     return render(
#         request,
#         "core/index.html",
#         context={
#             "skills": skills,
#             "projects": projects,
#             "jobs": jobs,
#             "educations": educations,
#             "interests": interests,
#             "certificates": certificates,
#         },
#     )
class HomeView(TemplateView):
    def get_template_names(self):
        return ["core/index.html"]

    def get_context_data(self, **kwargs):
        pass


home_view = HomeView.as_view()


class DownloadCView(views.View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join(os.getcwd(), "files/resume.pdf")
        return FileResponse(
            open(file_path, "rb"), as_attachment=True, filename="resume.pdf"
        )


download_cv_view = DownloadCView.as_view()
