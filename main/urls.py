from django.urls import path
from . import views

urlpatterns = [
    # path('list/users', views.list_users, name='list_users',),
    path('create/users', views.create_iqro_user, name='create/users')
]