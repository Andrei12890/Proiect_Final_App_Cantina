from django.urls import path
from cantina import views

app_name = 'cantina'

urlpatterns = [
    path('', views.CantinaView.as_view(), name='lista_cantina'),
    path('adaugare/', views.CreateCantinaView.as_view(), name='adaugare'),
    path('<int:pk>/editeaza/', views.UpdateCantinaView.as_view(), name='editeaza'),
    path('<int:pk>/anuleaza/', views.deactivate_cantina, name='anuleaza'),
    path('<int:pk>/comanda/', views.activate_cantina, name='comanda'),
]
