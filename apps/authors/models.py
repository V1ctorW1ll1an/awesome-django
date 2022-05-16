from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):

    class Expertise(models.TextChoices):
        BOOKS = 'BOOKS', _('Livros')
        ARTICLES = 'ARTICLES', _('Artigos')
        MAGAZINES = 'MAGAZINES', _('Revistas')
        MANGAS = 'MANGAS', _('Mangas')
        FILMS = 'FILMS', _('Filmes')

    default_auto_field = 'django.db.models.BigAutoField'
    first_name = models.CharField(
        max_length=30, null=False, blank=False, verbose_name="Nome", default='')
    last_name = models.CharField(
        max_length=30, null=False, blank=False, verbose_name="Sobrenome", default='')
    email = models.EmailField(null=False, blank=False,
                              verbose_name="E-mail", max_length=100, default='')
    password = models.CharField(
        null=False, blank=False, max_length=100, verbose_name="Senha", default='')
    phone = models.IntegerField(verbose_name="Telefone", null=True, blank=True)
    age = models.IntegerField(verbose_name="Idade", null=True, blank=True)
    salary = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Salário", blank=True, null=True)
    date_of_birth = models.DateField(
        "Data de aniversário", null=False, blank=False, default='')
    expertise = models.CharField(
        choices=Expertise.choices, verbose_name="Especialidade", max_length=100, null=False, blank=False, default='')
    cpf = models.IntegerField(
        verbose_name="Cpf", blank=False, null=False, default=0)
    state = models.CharField(verbose_name="Estado",
                             max_length=100, blank=True, null=True)
    city = models.CharField(verbose_name="Cidade",
                            max_length=100, blank=True, null=True)
    description = models.TextField(
        max_length=5000, verbose_name="Descrição", blank=True, null=True, default='')
    file = models.FileField(verbose_name="Anexo",
                            blank=True, null=True, upload_to="files/")
