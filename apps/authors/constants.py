from django.db import models
from django.utils.translation import gettext_lazy as _


class Expertise(models.TextChoices):
    BOOKS = 'BOOKS', _('Livros')
    ARTICLES = 'ARTICLES', _('Artigos')
    MAGAZINES = 'MAGAZINES', _('Revistas')
    MANGAS = 'MANGAS', _('Mangas')
    FILMS = 'FILMS', _('Filmes')
