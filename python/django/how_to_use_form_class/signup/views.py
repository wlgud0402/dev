from django.shortcuts import redirect, HttpResponse, HttpResponseRedirect, render
from django.contrib.auth.models import User
from how_to_use_form_class.forms import *
from django.template import RequestContext


def signup(request):
    return render(request, 'signup/signup.html')


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

        # variables = RequestContext(request, {
        #     'form': form
        # })

        return render(request, 'signup/register.html', {'form': form})
