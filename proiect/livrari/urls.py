from django.urls import path
from livrari import views

app_name = 'livrari'

urlpatterns = [
    path('adaugare/', views.CreateLivrariView.as_view(), name='adaugare_livrare'),
    path('', views.LivrariView.as_view(), name='lista_livrari'),
]
