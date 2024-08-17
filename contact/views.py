from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import ContactForm


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, "contact/contact.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            # TODO add send mail logic here

            form.save()
            messages.success(request, "Your message has been delivered successfully!")
            return HttpResponseRedirect(reverse("core:home"))

        return render(request, "contact/contact.html", context={"form": form})


contact_view = ContactView.as_view()
