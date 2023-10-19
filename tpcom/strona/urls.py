from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('about/', views.about, name="about"),   #jeśli damy path('about/', views.about, name="about"), to po wejściu na 'O firmie' mamy adres ../about/about
   path('contact/', views.contact, name="contact"),
   path('pricing/', views.pricing, name="pricing"),
   path('instrukcje/', views.instrukcje, name="instrukcje"),
   path('opismMedica/', views.opismMedica, name="opismMedica"),
   path('kursy/', views.kursy, name="kursy"),

]