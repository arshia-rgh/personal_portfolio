from django.shortcuts import render
from django.views import View


class ContactView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


contact_view = ContactView.as_view()
