from django import forms
from .models import Comment, Profile, Post, Business

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['username', 'neighbourhood', 'post_img']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['bus_owner','neighbourhood']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username', 'post']
    

