from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns =[
    # url('^$', views.welcome, name = 'welcome')
    path('', views.welcome, name = 'welcome'),
    # path('search/', views.search_results, name='search_results')t

]