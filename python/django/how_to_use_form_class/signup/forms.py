from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    username = forms.CharField(label='사용자이름', max_length=30)
    email = forms.EmailField(label='이메일')
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput())
    password2 = forms.CharField(label='비밀번호확인', widget=forms.PasswordInput())

    # 비밀번호 확인
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

    # 유저이름 확인
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):  # 정규표현식과 일치하지 않을경우 None을 반환함
            raise forms.ValidationError('사용자 이름은 알파벳, 숫자, 밑줄(_) 만 가능합니다.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:  # username으로 된 유저가 존재하지 않는다 => 이 username으로 가입이 가능하다.
            return username
        raise forms.ValidationError('이미 사용중인 사용자 이름입니다.')
