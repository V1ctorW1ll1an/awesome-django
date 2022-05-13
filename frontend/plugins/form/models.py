from cms.models import CMSPlugin
from django.db import models

# Create your models here.


class FormPlugin(CMSPlugin):
    title = models.CharField(max_length=80)
