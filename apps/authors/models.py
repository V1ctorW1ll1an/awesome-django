from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.authors.constants import Expertise
from apps.person.models import Person


class Author(Person):

    default_auto_field = 'django.db.models.BigAutoField'

    age = models.IntegerField(
        verbose_name=_("Idade"),
        null=True,
        blank=True
    )

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Salário"),
        blank=True,
        null=True
    )

    date_of_birth = models.DateField(
        verbose_name=_("Data de aniversário"),
        null=False,
        blank=False
    )

    expertise = models.CharField(
        choices=Expertise.choices,
        verbose_name=_("Especialidade"),
        max_length=100,
        null=False,
        blank=False
    )

    description = models.TextField(
        max_length=5000,
        verbose_name=_("Descrição"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Autor")
        verbose_name_plural = _("Autores")
