from django.shortcuts import render
from django.views.generic import CreateView


class ContactView(CreateView):
    pass


contact_view = ContactView.as_view()
