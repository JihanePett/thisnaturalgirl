from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('grayhair/', views.grayhair, name='grayhair'),
    path('contact/', views.contact, name='contact'),
]
