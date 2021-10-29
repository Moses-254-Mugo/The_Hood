from django.contrib import admin
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=100)
    court = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
    
    def create_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls, neihbourhood):
        hood = cls.objects.filter(neihbourhood=neihbourhood).delete()
        return hood

class Profile(models.Model):
    image = CloudinaryField('image')
    
    


















#  @classmethod
#     def search_by_title(cls,search_term):
#         news = cls.objects.filter(title__icontains=search_term)
#         return news
