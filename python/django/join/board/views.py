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
        # user가 존재하지 않는다면 ObjectDoesNotExist 에러 발생시킴
        return HttpResponse("do not exist user")
    return render(request, 'board/list_by_user.html', {"user": user, "boards": boards})


def board(request):
    # 내부적으로 시행하지만 join과는 원칙적으로 다르다. 많은 select문의 실행
    user = User.objects.get(id=1)
    print("유저: ", user)

    user_board = Board.objects.filter(user_id=user)
    print("찾은 유저의 글들 => filter 사용", user_board)

    boards_with_no_related = Board.objects.all()
    print("글전체 Board.objects.all", boards_with_no_related)

    join_user_board = Board.objects.select_related('user')
    print("select_related를 사용한 유저의 글들: ", join_user_board)

    prefetch_board_to_user = Board.objects.prefetch_related('user')
    print("prefetch_board_to_user : =>>>>", prefetch_board_to_user)

    boards = Board.objects \
        .select_related('user') \
        # .filter(user=user)
    return render(request, 'board/list.html', {
        "boards": boards,
        "boards_with_no_related": boards_with_no_related
    },)
    # <!-- {% for board_with_no related in boards_with_no_related %}
    # {{board_with_no related}} {% endfor %} -->
