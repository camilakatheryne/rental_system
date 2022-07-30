from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('register/', views.register, name='register_reservation'),
    path('validate_register_reservation', views.validate_register_reservation, name='validate_register_reservation'),
    path('register_rental/', views.register_rental, name="register_rental"),
    path('validate_register_rental', views.validate_register_rental, name="validate_register_rental")
]
