from django.db import models

# Create your models here.
class Carousel(models.Model):
  image = models.ImageField(upload_to='carousels')
  caption = models.CharField(max_length= 50)
  
class CV(models.Model):
  file = models.ImageField(upload_to='cv/')
  
  
class ArchProject(models.Model):
  image = models.ImageField(upload_to='projects')
  title = models.CharField(max_length=50)
  urlPath = models.URLField(max_length=1000)
  date = models.DateTimeField(auto_now_add=True)
  
  
  
class TechProject(models.Model):
  image = models.ImageField(upload_to='projects')
  title = models.CharField(max_length=50)
  urlPath = models.URLField(max_length=1000)
  date = models.DateTimeField(auto_now_add=True)
  
class BisProject(models.Model):
  image = models.ImageField(upload_to='projects')
  title = models.CharField(max_length=50)
  urlPath = models.URLField(max_length=1000)
  date = models.DateTimeField(auto_now_add=True)
