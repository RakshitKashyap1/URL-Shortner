from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/shorten/', views.api_shorten, name='api_shorten'),
    path('<str:short_code>', views.redirect_url, name='redirect'),
]
