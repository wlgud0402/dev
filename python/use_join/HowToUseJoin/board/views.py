from django.shortcuts import render, redirect, HttpResponse
from .models import Board, User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import json


# Create your views here.

def boards_by_user(request):
    try:
        user = User.objects.get(id=request.GET.get('id'))
        posts = user.post_set.all()
    except ObjectDoesNotExist:
        return HttpResponse("do not exist user")
    return render(request, 'board/list_by_user.html', {"user": user, "boards": boards})


def boards(request):
    # try:
    #     user = User.objects.get(id=request.GET.get('id'))
    # except ObjectDoesNotExist:
    #     return HttpResponse("do not exist user")

    # boards = Board.objects.all()
    # return render(request, 'board/list.html', { "boards": boards })

    boards = Board.objects \
        .select_related('user') \
        # .filter(user=user)
    return render(request, 'board/list.html', {"boards": boards})


def board(request):
    try:
        board = Board.objects.get(id=request.GET.get('id'))
    except ObjectDoesNotExist:
        return HttpResponse('do not exist post')
    return render(request, 'board/one.html', {"board": board})


def write(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    try:
        user = User.objects.get(id=2)
    except ObjectDoesNotExist:
        return HttpResponse("do not exist user")
    board = Board(user=user, title=title, content=content)
    board.save()
    return HttpResponse("success")


def join(request):
    name = request.GET.get('name')
    user = User(name=name)
    user.save()
    return HttpResponse("success")
