from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"), #index
    path('index', views.index, name="index"), #index
    path('header', views.header, name="header"), #header
    path('footer', views.footer, name="footer"), #footer
    path('contactus', views.contactus, name="contactus"), #contactus forn




    #for testing perpose ("it's not recomended for me")
    # path('newsarea', views.newsarea, name="newsarea"), #news_area
    # path('topfarea', views.topfarea, name="topfarea"), #top_area
    # path('header', views.header, name="header"), #header
    # path('touchslide', views.touchslide, name="touchslide"), #header
    # path('footer', views.footer, name="footer"), #footer

]
