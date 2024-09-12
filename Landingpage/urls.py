from django.contrib import admin
from django.urls import path,include
from Landingpage import views



admin.site.site_header="Login My services"
admin.site.site_title = "Welcome to Samir's Dashboard"
admin.site.index_title = "Welcome to this portal"





urlpatterns = [
    path('', views.home, name='home'),
    path('about', views .about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]