from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_users, name="login"),
    path('logout/', views.logout, name="logout"),
]
