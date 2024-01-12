from django.urls import path
from . import views

urlpatterns = [
    path('cr/user/', views.create_user),
    path('upgruser/', views.upgruser),
    path('ls/usr/', views.list_users),
]
