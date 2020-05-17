from django.urls import path

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='main'),
    path('afisha/<film>', views.afisha, name='afisha'),
    path('afisha/', views.afisha, name='afisha'),
    path('accounts/login/', views.login_view, name='login_view'),
    path('accounts/logout/', views.logout_view, name='logout_view'),
]
urlpatterns += staticfiles_urlpatterns()