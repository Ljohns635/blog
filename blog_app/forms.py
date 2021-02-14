from django import forms
from blog_app.models import SubscribePage,SuggestPage


class SubscribePageForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)

class SuggestPageForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    subject = forms.CharField(max_length=150)
    body = forms.CharField(widget=forms.Textarea)
    