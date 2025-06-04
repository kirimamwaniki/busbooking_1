from django.urls import path
from . import views

urlpatterns = {
    path('testing/', views.testing, name="testing"),
    path('', views.main, name='main'),
    path('success/', views.success, name='success'),
}