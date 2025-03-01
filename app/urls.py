from django.urls import path
from . import views

urlpatterns = [
    path ('comparar/', views.Comparar_Moeda, name='Comparar_Moeda'),
]