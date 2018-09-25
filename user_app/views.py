from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == '' or password == '':
            return render(request, 'index.html', {"error": "账号或密码不能为空！"})
        if username == 'admin' and password == 'admin':
            return render(request,'login_action.html')
        if username != 'admin' or password != 'admin':
            return render(request, 'index.html', {"error": "账号或密码错误，请重新输入！"})
    else:
        return render(request, 'index.html')
