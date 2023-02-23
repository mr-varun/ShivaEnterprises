from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('ulogin/',views.login_user, name='ulogin'),
    path('alogin/',views.login_admin, name='alogin'),
    path('register/',views.register_user, name='register'),
    path('logout/',views.logout_user, name='logout'),
]
