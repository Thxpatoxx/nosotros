from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('list', views.post_list, name='post_list'),
    path('pacient', views.post_list_pacient, name='post_list_pacient'),
    path('users', views.user_list, name='user_list'),
    ###
    path('Diagnostico/<int:pk>/', views.post_detail, name='post_detail'),
    path('Paciente/<int:pk>/', views.post_detail_pacient, name='post_detail_pacient'),
    ###
    path('Diagnostico/new', views.post_new, name='post_new'),
    path('Diagnostico/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('Paciente/new', views.post_new_pacient, name='post_new_pacient'),
    path('Paciente/<int:pk>/edit/', views.post_edit_pacient, name='post_edit_pacient'),
    ###
    path('accounts/', include('django.contrib.auth.urls')),
]