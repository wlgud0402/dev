from django.contrib import admin
from board.models import User, Board

# Register your models here.


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content',)


@admin.register(User)
class Userdmin(admin.ModelAdmin):
    list_display = ('name',)
