from django.urls import path
from . import views

urlpatterns = [
    path('', views.serials_home, name='serials_home')
]
