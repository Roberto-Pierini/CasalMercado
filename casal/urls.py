from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/',views.cadastro ),
    path('login/',views.logar),
    path('home/',views.home),
    path('logout/',views.deslogar)
]