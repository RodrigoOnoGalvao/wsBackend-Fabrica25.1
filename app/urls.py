from django.urls import path
from .views import (
    PessoaListView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView, PessoaDetailView,
    MoedaListView, MoedaCreateView, MoedaUpdateView, MoedaDeleteView, MoedaDetailView, index
)

urlpatterns = [
    path('', index, name='index'),
    path('pessoas/', PessoaListView.as_view(), name='pessoa_list'),
    path('pessoas/create/', PessoaCreateView.as_view(), name='pessoa_create'),
    path('pessoas/update/<int:pk>/', PessoaUpdateView.as_view(), name='pessoa_update'),
    path('pessoas/delete/<int:pk>/', PessoaDeleteView.as_view(), name='pessoa_delete'),
    path('pessoas/detail/<int:pk>/', PessoaDetailView.as_view(), name='pessoa_detail'),

    path('moedas/', MoedaListView.as_view(), name='moeda_list'),
    path('moedas/create/', MoedaCreateView.as_view(), name='moeda_create'),
    path('moedas/update/<int:pk>/', MoedaUpdateView.as_view(), name='moeda_update'),
    path('moedas/delete/<int:pk>/', MoedaDeleteView.as_view(), name='moeda_delete'),
    path('moedas/detail/<int:pk>/', MoedaDetailView.as_view(), name='moeda_detail'),
]
