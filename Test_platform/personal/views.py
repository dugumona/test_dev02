from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#MTV  --V view文件

def say_hello(request):
    #print("say_hello")
    input_name = request.GET.get("name", "")
    return render(request, "index.html", {"name": input_name})

def index(request):
    print(request.method)
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print(username)
        print(password)
        msg = "用户名或密码为空"

        if username == "" or password == "":
            # return HttpResponse(msg)
            return render(request, "index.html", {"error": "用户名或密码为空"})
        if username == "admin" and password == "admin123":
            return HttpResponse("登录成功")
        else:
            return render(request, "index.html", {"error": "用户名或密码错误"})


# def login_action(request):
#     username = request.POST.get("username", "")
#     password = request.POST.get("password", "")
#     print(username)
#     print(password)
#     msg = "用户名或密码为空"
#
#     if username == "" or password == "":
#         #return HttpResponse(msg)
#         return  render(request, "index.html", {"error": "用户名或密码为空"})
#     if username =="admin" and password =="admin123":
#         return HttpResponse("登录成功")
#     else:
#         return render(request, "index.html", {"error": "用户名或密码错误"})

    #return render(request, "login_action.html")