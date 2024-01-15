from django.urls import path
from . import views

urlpatterns = [
    path('cr/user/', views.create_user),
    path('upgruser/<int:id>', views.upgruser),
    path('ls/usr/', views.list_users),
    path('del/usr/<int:id>', views.del_user),
]
