from django.test import TestCase
from django.db.models import fields
from core.models import Skill, Project, JobExperience, Education, Interest, Certificate


class BaseModelTestCase:
    model = None
    fields = {}
    fields_2 = {}

    def test_create_instance(self):
        instance = self.model._default_manager.create(**self.fields)
        self.assertIsNotNone(instance.pk)


class SkillModelTestCase(TestCase):
    pass


class ProjectModelTestCase(TestCase):
    pass


class JobExperienceModelTestCase(TestCase):
    pass


class EducationModelTestCase(TestCase):
    pass


class InterestModelTestCase(TestCase):
    pass


class CertificateModelTestCase(TestCase):
    pass
