from django.urls import path
from . import views




urlpatterns = [
    path('', views.rrt , name='kino'),
     path('info/', views.ttr , name='info')
]