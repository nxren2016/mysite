# encoding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("欢迎你！登录成功！！")
            else:
                return HttpResponse("对不起，你的账号或密码错误！！")
        else:
            return HttpResponse("无效登录！")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"from": login_form})

