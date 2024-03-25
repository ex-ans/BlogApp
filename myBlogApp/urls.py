from django.contrib import admin
from django.urls import path
from myBlogApp import views
urlpatterns = [
    path('' , views.index , name='index'),
    path('home' , views.home , name='home'),
    path('createblog' , views.createblog , name='createblog'),
    path('uploadedblog' , views.uploadedblog , name='uploadedblog'),
    path('signin' , views.signin , name='signin'),
    path('signup' , views.signup , name='signup'),
    path('logoutuser' , views.logoutuser , name='logoutuser'),
    path('readmore/<int:blog_id>' , views.readmore , name='readmore'),
    path('delete/<int:blog_id>' , views.delete , name='delete'),
    path('search' , views.search , name='search'),
    path('edit/<int:blog_id>' , views.edit , name='edit'),
    path('edit/updated/<int:blog_id>' , views.updated , name='updated'),
]
