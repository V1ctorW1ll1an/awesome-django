from django import forms

from apps.authors.models import Author


class AuthorCustomForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
