from django.urls import path
from livrari import views

app_name = 'livrari'

urlpatterns = [
    path('adaugare/', views.CreateLivrariView.as_view(), name='adaugare_livrare'),
    path('', views.LivrariView.as_view(), name='lista_livrari'),
    path('<int:pk>/editeaza/', views.UpdateLivrariView.as_view(), name='editeaza'),
    path('<int:pk>/anuleaza/', views.deactivate_livrari, name='anuleaza'),
    path('<int:pk>/comanda/', views.activate_livrari, name='comanda'),
]
