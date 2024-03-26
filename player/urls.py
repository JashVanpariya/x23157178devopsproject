from django.urls import path

from . import views

urlpatterns = [

    path('', views.players_list, name='players-list'),

    path('create/', views.create_player, name='create-player'),

    path('edit/<int:player_id>/', views.edit_player, name='edit-player'),

    path('delete/<int:player_id>/', views.delete_player, name='delete-player')

]