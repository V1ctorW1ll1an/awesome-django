from django.db import models

# Create your models here.


class Person(models.Model):
    default_auto_field = 'django.db.models.BigAutoField'
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
