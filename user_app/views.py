from django.contrib.auth.decorators import login_required
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
            response = HttpResponseRedirect('/project_manage/')
            # response.set_cookie('user', username, 3600)  # 添加浏览器 cookie
            request.session['user'] = username  # 将 session 信息记录到浏览器
            return response
            # return render(request, 'templates/project_manage.html')
        else:
            return render(request, 'index.html', {"error": "账号或密码错误！"})
    else:
        return render(request, 'index.html')


@login_required
def project_manage(request):
    # username = request.COOKIES.get('user', '') #读取浏览器 cookie
    username = request.session.get('user', '')  # 读取浏览器 session
    return render(request, 'project_manage.html', {"username": username})


@login_required
def logout(request):
    auth.logout(request)  # 退出登录
    response = HttpResponseRedirect('/')
    return response
