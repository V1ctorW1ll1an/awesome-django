from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.person.mixins import AddressMixin, ContactMixin

# Create your models here.


class Person(AddressMixin, ContactMixin):
    default_auto_field = 'django.db.models.BigAutoField'

    username = models.CharField(
        verbose_name=_('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        }
    )

    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=150,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=150,
        blank=True,
        null=True
    )

    email = models.EmailField(
        verbose_name=_("Email"),
        unique=True,
        blank=False,
        null=False
    )

    cpf = models.IntegerField(
        verbose_name=_("Cpf"),
        blank=False,
        null=False,
        unique=False
    )

    class Meta:
        verbose_name = _('Pessoa')
        verbose_name_plural = _('Pessoas')
        abstract = True
