from django.contrib import admin
from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('listar/', views.PruebaListView.as_view()),
]
