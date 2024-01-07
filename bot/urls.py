from django.urls import path
from . import views

urlpatterns = [
    path('a/l_person',views.arrived_left_person, name='arrive_left_person' ),
    path('list/turniket/pupil', views.list_turniket_pupil, name='list_turniket_pupil'),
    path('list/turniket/users', views.list_turniket_users, name='list_turniket_users'),
]