from django.urls import path
from . import views

urlpatterns = [
    path('register1/register/', views.register, name='register'),
    path('register1/login/', views.login, name='login'),
    path('register1/aboutus/', views.aboutus, name='aboutus'),
    path('register1/checkout/', views.checkout, name='checkout'),
    path('register1/order/', views.order, name='order'),
    path('register1/homepage/', views.homepage, name='homepage'),
    path('register1/logout/', views.logout, name='logout'),
]
