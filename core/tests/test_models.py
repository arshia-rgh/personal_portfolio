from unittest import skip

from django.utils import timezone
from django.test import TestCase
from core.models import (
    Skill,
    Project,
    JobExperience,
    # Education, Interest, Certificate
)


class BaseModelTestCase:
    model = None
    # should contain only non default fields
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

    def test_default_values(self):
        instance = self.model(**self.fields)
        for field in self.model._meta.fields:
            if field.has_default():
                self.assertEqual(getattr(instance, field.name), field.default)


class SkillModelTestCase(BaseModelTestCase, TestCase):
    model = Skill
    fields = {"name": "python", "logo": None}
    fields_2 = {"name": "django", "logo": None}


class ProjectModelTestCase(BaseModelTestCase, TestCase):
    model = Project

    fields = {
        "name": "RPC",
        "source_link": "www.example.com",
        "live_link": None,
        "description": "TEST PROJECT",
        "status": "Ongoing",
    }
    fields_2 = {
        "name": "RPC_2",
        "source_link": "www.example2.com",
        "live_link": None,
        "description": "TEST PROJECT2",
        "status": "Ongoing",
    }


class JobExperienceModelTestCase(BaseModelTestCase, TestCase):
    model = JobExperience
    fields = {
        "company_name": "Digitoon",
        "position": "Back end developer",
    }
    fields_2 = {
        "company_name": "Digitoon",
        "position": "DevOps engineer",
    }

    def test_str_representation(self):
        instance = self.model(**self.fields)
        self.assertEqual(str(instance), instance.company_name + " " + instance.position)

    def test_custom_save_logic(self):
        instance = self.model._default_manager.create(**self.fields)
        self.assertEqual(instance.end_date.hour, timezone.now().hour)

    @skip
    def test_years_of_experience_property(self):
        # TODO years_of_experience bug should be fixed

        instance1 = self.model._default_manager.create(
            company_name="test",
            position="Test position",
            start_date=timezone.datetime(2019, 8, 1),
            end_date=timezone.datetime(2020, 1, 11),
        )
        self.assertEqual(instance1.years_of_experience, 1)


class EducationModelTestCase(TestCase):
    pass


class InterestModelTestCase(TestCase):
    pass


class CertificateModelTestCase(TestCase):
    pass
