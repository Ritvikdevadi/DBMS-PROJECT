from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('main', views.main, name='main'),
    path('testing', views.testing, name='testing'),   
    path('app', views.members, name='app'),
    path('app/details/<int:id>', views.details, name='details'),
]