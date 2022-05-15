# Create your models here.
from cms.models import CMSPlugin
from django.db import models


class AuthorCustomFormPluginModel(CMSPlugin):
    title = models.CharField(max_length=80)
