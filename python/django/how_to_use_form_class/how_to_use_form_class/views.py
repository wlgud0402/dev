from django.shortcuts import render, redirect, HttpResponse, reverse, HttpResponseRedirect
from django.contrib.auth.models import User
from how_to_use_form_class.forms import *


def signup(request):
    return HttpResponse("signup 페이지")


def register_page(request):
    if request.method == 'POST':  # 받아온 데이터를 내가만든 RegistrationForm에 넣는다
        form = RegistrationForm(request.POST)
        if form.is_valid():  # 올바른 형태인지
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/')
        else:
            form = RegistrationForm()

        return render(request, 'how_to_use_form_class/register.html', {'form': form, })
