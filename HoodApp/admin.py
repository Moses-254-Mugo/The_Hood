from django.contrib import admin
from .models import Neighbourhood, Profile, Post, Police, Health, Business


# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Police)
admin.site.register(Health)
admin.site.register(Business)