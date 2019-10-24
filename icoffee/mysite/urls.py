from django.urls import path
from . import views

urlpatterns = [
    path('', views.wow, name='wow'),
    path('instagram', views.instagram, name='instagram'),
    path('mercadolibre', views.mercadolibre, name='mercadolibre'),
    path('facebook', views.facebook, name='facebook'),
    path('pagamenos', views.pagamenos, name='pagamenos'),
    path('wow', views.wow, name='wow'),
    path('gold', views.gold, name='gold'),
    path('offer', views.offer, name='offer'),
    path('characters', views.characters, name='characters'),
    path('leveling', views.leveling, name='leveling'),
    path('summary', views.summary, name='summary'),
    path('buy', views.buy, name='buy'),
    path('sell', views.sell, name='sell'),
    path('contact', views.contact, name='contact')
]
