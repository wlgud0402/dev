from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name='board'),
    path('user/', views.boards_by_user, name='boards_by_user')
]
