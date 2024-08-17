from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.contrib import messages


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, "contact/contact.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.body)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            # TODO add send mail logic here

            messages.success(request, "Your message has been delivered successfully!")
            return HttpResponseRedirect(reverse("core:home"))

        return render(request, "contact/contact.html", context={"form": form})


contact_view = ContactView.as_view()
