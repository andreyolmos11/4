from django.urls import path
from . import views

app_name = 'citas'
urlpatterns = [
    path('', views.lista_citas, name='lista_citas'),
    path('<int:cita_id>/', views.detalle_cita, name='detalle_cita'),
]
