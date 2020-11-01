from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
import re

urlpatterns = [
    path('signup/', views.signup),
    path('register/', views.register_page),
]
