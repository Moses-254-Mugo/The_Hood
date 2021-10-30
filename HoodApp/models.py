from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.contrib.auth.models import User

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
    name = models.CharField(max_length=40)
    description = HTMLField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Post(models.Model):
    post_img = CloudinaryField('image')
    post = HTMLField()
    title = models.CharField(max_length=200)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    username  = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
class Business(models.Model):
    name= models.CharField(max_length=150)
    email = models.EmailField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    bus_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = HTMLField()
    

    def __str__(self):
        return self.name

class Health(models.Model):
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.address



class Police(models.Model):
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.comment













#  @classmethod
#     def search_by_title(cls,search_term):
#         news = cls.objects.filter(title__icontains=search_term)
#         return news
