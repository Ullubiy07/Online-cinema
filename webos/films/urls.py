from django.urls import path
from . import views

urlpatterns = [
    path('', views.films_home, name='films_home'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.FilmsDetailView.as_view(), name='films_detail'),
    path('<int:pk>/update', views.FilmsUpdateView.as_view(), name='films_update'),
    path('<int:pk>/delete', views.FilmsDeleteView.as_view(), name='films_delete')
]
