from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('instagram', views.instagram, name='instagram'),
    path('mercadolibre', views.mercadolibre, name='mercadolibre'),
]