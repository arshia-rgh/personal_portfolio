from django.test import TestCase
from core.models import Skill, Project, JobExperience, Education, Interest, Certificate


class BaseModelTestCase:
    model = None
    fields = {}
    fields_2 = {}

    def test_create_instance(self):
        instance = self.model._default_manager.create(**self.fields)
        self.assertIsNotNone(instance.pk)

    def test_ordering(self):
        instance1 = self.model._default_manager.create(**self.fields)
        instance2 = self.model._default_manager.create(**self.fields_2)
        instances = self.model._default_manager.all()

        self.assertEqual(list(instances), [instance2, instance1])

    def test_str_representation(self):
        instance = self.model(**self.fields)
        self.assertEqual(str(instance), instance.name)


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
