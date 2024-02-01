from django.urls import path
from . import views

urlpatterns = [
    path('cr/user/', views.create_user),
    path('upgruser/<int:id>', views.upgruser),
    path('ls/usr/', views.list_users),
    path('del/usr/<int:id>', views.del_user),
    path('list/school', views.list_school),
    path('crt/schl', views.crt_schl),
    path('upgr/schl/<int:id>', views.upd_schl),
    path('del/schl/<int:id>', views.d_schl),
    #don`t tested
    path('list/sub', views.list_subject),
    path('crt/sub', views.cr_sbjct),
    path('upgr/sub/<int:id>', views.upd_sbjct),
    path('del/sub/<int:id>', views.del_sub),
    path('list/class', views.list_class),
    path('crt/class/', views.crt_clss),
    path('upg/class/<int:id>', views.upd_clss),
    path('del/class/<int:id>', views.del_clss),
    path('list/parent/', views.list_par),
    path('crt/parent/', views.crt_parnt),
    path('upg/parent/<int:id>', views.upd_par),
    path('del/parent/<int:id>', views.d_par),
]
