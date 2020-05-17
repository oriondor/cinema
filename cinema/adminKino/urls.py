from django.urls import path

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('films', views.films, name='films'),
    path('film/<film_id>', views.film, name='film'),
    path('delete/<del_id>', views.delete, name='delete'),
    path('', views.home, name='home'),
]
urlpatterns += staticfiles_urlpatterns()