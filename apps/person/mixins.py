from pathlib import Path

from common.hash_paths import file_hash_path, image_hash_path
from django.db import models
from django.utils.translation import gettext_lazy as _


class AddressMixin(models.Model):

    postal_code = models.CharField(
        verbose_name=_("CEP"),
        max_length=11,
    )

    street = models.CharField(
        verbose_name=_("Endereço"),
        max_length=200,
    )

    number = models.CharField(
        verbose_name=_("Número"),
        max_length=30,
    )

    complement = models.CharField(
        verbose_name=_("Complemento"),
        max_length=100,
        null=True,
        blank=True,
    )

    city = models.CharField(
        verbose_name=_("Cidade"),
        max_length=100,
    )

    state = models.CharField(
        verbose_name=_("Estado"),
        max_length=100,
    )

    class Meta:
        abstract = True


class ContactMixin(models.Model):

    cel_phone = models.CharField(
        verbose_name=_("Celular"),
        max_length=15
    )

    class Meta:
        abstract = True


class Image(models.Model):
    image = models.ImageField(
        verbose_name=_("Imagem"),
        upload_to=image_hash_path,
        null=True,
        blank=True,
    )

    def __str__(self):
        if not self.image:
            return str(self.pk)

        return self.filename

    @property
    def filename(self):
        return Path(self.image.file.name).name

    @property
    def serialized(self):
        return {
            "id": self.pk,
            "image": f'<img src="{self.image.url}">',
            "content": {
                "name": self.filename,
                "url": self.image.url,
            },
        }


class File(models.Model):

    file = models.FileField(
        upload_to=file_hash_path,
        null=True,
        blank=True,
    )

    def __str__(self):
        if not self.file:
            return str(self.pk)

        return self.filename

    @property
    def filename(self):
        return Path(self.file.file.name).name

    @property
    def serialized(self):
        return {
            "id": self.pk,
            "icon": '<div class="file-field-item--icon"><i class="fa-solid fa-file-zipper"></i></div>',
            "content": {
                "name": self.filename,
                "url": self.file.url,
            },
        }
