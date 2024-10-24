from django.urls import path
from cantina import views

app_name = 'cantina'

urlpatterns = [
    path('adaugare/', views.CreateCantinaView.as_view(), name='adaugare'),
]
