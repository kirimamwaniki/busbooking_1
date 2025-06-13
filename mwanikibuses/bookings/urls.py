from django.urls import path
from . import views

urlpatterns = [
    path('testing/', views.testing, name='testing'),
    path('', views.main, name='main'),
    path('success/', views.success, name='success'),
    path('pay/<int:id>', views.payment, name='pay'),
]