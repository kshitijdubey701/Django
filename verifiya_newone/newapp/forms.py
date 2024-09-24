# forms.py

from django import forms
from .models import InternshipApplication
from .models import Contact

class InternshipForm(forms.ModelForm):
    class Meta:
        model = InternshipApplication
        fields = ['full_name', 'email', 'sex', 'whatsapp_number', 'college_name', 'qualification', 'last_qualification_year', 'resume']


from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']