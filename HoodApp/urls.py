from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns =[
    # url('^$', views.welcome, name = 'welcome')
    path('', views.index, name = 'index'),
    path('my-profile/', views.myProfile, name='my-profile'),
    # path('search/', views.search_results, name='search_results')t

]