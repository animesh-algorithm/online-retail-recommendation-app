from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:desc>/<int:qty>/<str:price>/<int:country>', views.recommend, name='recommend')
]
