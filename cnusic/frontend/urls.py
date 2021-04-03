from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.index),
    path('join', views.index),
    path('create', views.index),
]
