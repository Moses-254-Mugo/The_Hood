from collections import namedtuple
from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns =[
    path('', views.index, name = 'index'),
    path('my-profile/', views.myProfile, name='my-profile'),
    path('create/profile', views.New_profile, name='new-profile'),
    path('update/profile',views.update_profile, name='update_profile'),
    path('health', views.well_being, name="health"),
    path('authorities', views.authorities, name="authorities"),
    path('post', views.posts, name="post"),
    path('new/post', views.Newpost, name="new_post"),
    path('business', views.business, name='business'),
    path('new/business',views.create_new_business,name='new_business')
    
    
    # path('search/', views.search_results, name='search_results')t

]