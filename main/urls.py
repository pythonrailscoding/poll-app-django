from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('vote/<int:pk>/', views.vote, name='vote'),
    path('results/<int:pk>/', views.results, name='results'),
]
