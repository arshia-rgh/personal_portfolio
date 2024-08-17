from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import ContactForm
from .tasks import send_email


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(
            request,
            "contact/contact.html",
            context={"form": form, "title": "ContactMe"},
        )

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["body"]

            try:
                send_email.delay(email=email, name=name, message=message)
            except Exception as e:
                send_mail(
                    subject="Thank you for contacting us",
                    message=f"Hi {name},\n\nThank you for reaching out to me. I have received your message:\n\n{message}\n\nBest regards,\nArshia.rgh",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[
                        email,
                    ],
                    fail_silently=False,
                )

            form.save()
            messages.success(request, "Your message has been delivered successfully!")
            return HttpResponseRedirect(reverse("core:home"))

        return render(
            request,
            "contact/contact.html",
            context={"form": form, "title": "ContactMe"},
        )


contact_view = ContactView.as_view()
