from django.urls import path
from . import views

urlpatterns = [
    path('', views.gerar),
    path('certificado/<str:cpf>/', views.certificado),
]