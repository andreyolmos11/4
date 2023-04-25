from django.urls import path
from . import views

urlpatterns = [
    path('factura/nueva/', views.factura_nueva, name='factura_nueva'),
    path('factura/editar/<int:pk>/', views.factura_editar, name='factura_editar'),
    path('factura/detalle/<int:pk>/', views.factura_detalle, name='factura_detalle'),
]
