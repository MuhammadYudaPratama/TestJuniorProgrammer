from django.urls import path
from . import views

urlpatterns = [
    path('', views.produk_list, name='produk_list'),
    path('bisa-dijual/', views.produk_bisa_dijual, name='produk_bisa_dijual'),
    path('tambah/', views.tambah_produk, name='tambah_produk'),
    path('edit/<int:id>/', views.edit_produk, name='edit_produk'),
    path('hapus/<int:id>/', views.hapus_produk, name='hapus_produk'),
]
