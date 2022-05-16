from django import forms

from apps.authors.models import Author


class AuthorCustomForm(forms.ModelForm):
    # first_name = forms.CharField(label=u'Nome', required=True)
    # last_name = forms.CharField(label=u'Sobrenome', required=True)

    class Meta:
        model = Author
        fields = '__all__'
        # Alterar as props dos campos
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome'
        }

        error_messages = {
            'first_name': {
                'max_length': 'Maximo 30 caracteres!'
            },
            'last_name': {
                'max_length': 'Maximo 30 caracteres!'
            }
        }

        # Atributos dos fields criados
        widget = {
            'first_name': forms.TextInput(attrs={}),
            'last_name': forms.TextInput(attrs={})
        }
