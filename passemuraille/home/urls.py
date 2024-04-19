from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('introduction_enquete/<int:id_enquete>/', views.introduction_enquete, name='introduction_enquete'),
    path('centrale_enquete/<int:id_enquete>/', views.centrale_enquete, name='centrale_enquete'),
    path('indice_enigme_chiffres/<int:id_indice_chiffres>/', views.indice_enigme_chiffres, name='indice_enigme_chiffres'),
    path('indice_enigme_autre/<int:id_indice_autre>/', views.indice_enigme_autre, name='indice_enigme_autre'),
    path('indice_chiffres_ouverte/<int:id_indice_chiffres>/', views.indice_chiffres_ouverte, name='indice_chiffres_ouverte'),
    path('indice_autre_ouverte/<int:id_indice_autre>/', views.indice_autre_ouverte, name='indice_autre_ouverte'),
    path('timer/', views.countdown_timer, name='countdown_timer')
]