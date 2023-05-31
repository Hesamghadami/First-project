from django import forms
from .models import *


#class NewsletterForm(forms.Form):
#    email = forms.EmailField()



class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ['email']

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']