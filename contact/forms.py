from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput())
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea())
