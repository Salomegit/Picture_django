from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True,blank=True,upload_to="images/")