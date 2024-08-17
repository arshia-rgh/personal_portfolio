from django.test import TestCase

from contact.models import Message
from utils.base_model_test import BaseModelTestCase


class MessageModelTestCase(BaseModelTestCase, TestCase):
    model = Message
    fields = {
        "name": "ali",
        "email": "test@email.com",
        "title": "test title",
        "body": "test body",
    }
    fields_2 = {
        "name": "naghi",
        "email": "test.2@email.com",
        "title": "test title 2 ",
        "body": "test body 2 ",
    }

    def test_str_representation(self):
        instance = self.model(**self.fields)
        self.assertEqual(str(instance), instance.email + " " + instance.title)
