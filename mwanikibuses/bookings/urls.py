from django.urls import path
from . import views

urlpatterns = [
    path('testing/', views.testing, name='testing'),
    path('', views.main, name='main'),
    path('pay/<int:id>', views.payment, name='pay'),
    path('details/<int:id>', views.details, name="details"),
]