from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('about/', views.about, name='about'),
]
