from django.test import TestCase
from django.urls import reverse

from core.models import Skill


class HomeViewTestCase(TestCase):
    def test_template_render(self):
        response = self.client.get(reverse("core:home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/index.html")

    def test_context_data(self):
        response = self.client.get(reverse("core:home"))

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context["title"])
        self.assertIsNotNone(response.context["skills"])
        self.assertIsNotNone(response.context["projects"])
        self.assertIsNotNone(response.context["jobs"])
        self.assertIsNotNone(response.context["educations"])
        self.assertIsNotNone(response.context["interests"])
        self.assertIsNotNone(response.context["certificates"])

    def test_specific_context_values(self):
        Skill.objects.create(name="Python", priority=1)
        response = self.client.get(reverse("core:home"))

        self.assertEqual(response.status_code, 200)
        self.assertIn("Python", [skill.name for skill in response.context["skills"]])


class DownloadCVViewTestCase(TestCase):
    def test_file_download(self):
        response = self.client.get(reverse("core:download_cv"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")
