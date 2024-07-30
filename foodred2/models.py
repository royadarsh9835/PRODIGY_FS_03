# models.py
from django.db import models

class Redfood(models.Model):
    img = models.ImageField(upload_to='pics')

