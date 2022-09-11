from django.urls import path
from . import views

urlpatterns = [
path('ventas/', views.ventas_view, name='Ventas'),
path('refacciones/', views.refacciones_view, name='Refacciones'),
path('add_refacciones/', views.refacciones_view, name='AddRefacciones'),
path('edit_refacciones/', views.refacciones_view, name='EditRefacciones'),
path('delete_refacciones/', views.refacciones_view, name='DeleteRefacciones'),
]