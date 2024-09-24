from django.urls import path
from . import views  # Import your views from the app

urlpatterns = [
    path('home', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='Services'),
    path('team/', views.team, name='team'),
    path('internship/', views.internship_application_view , name='internship'),
    path('login/', views.login_view, name='login'),
    path('home/', views.index, name='search'),
    path('home/', views.index, name='subscribe_newsletter'),
    path('home/', views.index, name='home'),
    
   
]
