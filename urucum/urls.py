from django.urls import path
from urucum.views import index, cardapio

urlpatterns = [
    path('', index, name='index'),
    path('cardapio/', cardapio, name='cardapio')
]