from django.shortcuts import render, redirect, HttpResponse
from .models import Board, User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import json


def boards_by_user(request):
    try:
        user = User.objects.get(id=request.GET.get('id'))
        # (1:N)유저가 여러개의 글을 썼을경우 => 그 유저의 글들을 가져온다. 유저.글들_set.all()
        boards = user.board_set.all()
    except ObjectDoesNotExist:
        return HttpResponse("do not exist user")
    return render(request, 'board/list_by_user.html', {"user": user, "boards": boards})


def board(request):
    # 내부적으로 시행하지만 join과는 원칙적으로 다르다. 많은 select문의 실행
    boards_with_no_related = Board.objects.all()

    boards = Board.objects \
        .select_related('user') \
        # .filter(user=user)
    return render(request, 'board/list.html', {
        "boards": boards,
        "boards_with_no_related": boards_with_no_related
    })
