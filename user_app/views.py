from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth


# Create your views here.

def index(request):
    return render(request, 'index.html')


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(username=username, password=password)
        if username == '' or password == '':
            return render(request, 'index.html', {"error": "账号或密码不能为空！"})
        if user is not None:
            auth.login(request, user)
            return render(request, 'project_manage.html')
        else:
            return render(request, 'index.html', {"error": "账号或密码错误！"})
    else:
        return render(request, 'index.html')
