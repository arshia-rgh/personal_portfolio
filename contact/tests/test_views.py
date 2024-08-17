from django.contrib.messages import get_messages, constants
from django.test import TestCase, override_settings
from django.urls import reverse

from contact.models import Message


class ContactViewTestCase(TestCase):
    def test_get(self):
        response = self.client.get(reverse("contact:contact_form"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
        self.assertIsNotNone(response.context["form"])

    def test_post_create_instance(self):
        response = self.client.post(
            reverse("contact:contact_form"),
            data={
                "name": "ali",
                "email": "test@email.com",
                "title": "test title",
                "body": "body",
            },
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Message.objects.filter(name="ali").exists())

    @override_settings(
        MESSAGE_STORAGE="django.contrib.messages.storage.cookie.CookieStorage"
    )
    def test_post_add_messages(self):
        response = self.client.post(
            reverse("contact:contact_form"),
            data={
                "name": "ali",
                "email": "test@email.com",
                "title": "test title",
                "body": "body",
            },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].level, constants.SUCCESS)
        self.assertEqual(
            messages[0].message, "Your message has been delivered successfully!"
        )
