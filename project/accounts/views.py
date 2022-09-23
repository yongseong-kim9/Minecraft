from getpass import getuser
from http.client import HTTPResponse
import json
from multiprocessing import context
from re import template
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import User as U





# Create your views here.
# 회원가입
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        if request.POST['pw'] == request.POST['pw2']:
            user = U.objects.create(
                                            id=request.POST['id'],
                                            pw=request.POST['pw'],
                                            email=request.POST['email'],)
            return redirect('index')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

@csrf_exempt
def index(request):
    return render(request, 'index.html')

# # 회원가입
# # UserCreationForm
# # @csrf_exempt 
# # def signup2(request): 
# #     if request.method == 'POST': 
# #         if request.POST['password1'] == request.POST['password2']: 
# #             user = User.objects.create_user( 
# #                 username=request.POST['username'], 
# #                 password=request.POST['password1'], 
# #                 email=request.POST['email'],
# #             ) 
# #             auth.login(request, user) 
# #             return redirect('/') 
# #         return render(request, 'signup.html') 
# #     else: 
# #         form = UserCreationForm 
# #         return render(request, 'signup.html', {'form':form})


# 로그인
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['pw']
        # request.session['loginOK'] = False
        # user = authenticate(username=username, password=password)

        # print(user)
        # if user is not None:
        #     print("회원정보없음")
        #     return redirect('/login')
        # else:
        #     print("회원정보있음")
        if U.objects.filter(id=username).exists():
            getUser = U.objects.get(id=username)
            if getUser.pw == password:
                request.session['loginOK'] = True
                if request.session['loginOK'] == True:

                    return redirect('index')           
        else:
             return render(request,'login.html')
    
    else:
        return render(request,'login.html')


# # 로그아웃
# @csrf_exempt
# def logout(request):
#     auth.logout(request)
#     return redirect('index')




# 데이터 베이스 출력

def user_view(request):
    users = U.objects.all()
    print("users")
    return render(request, 'index.html',{'users':users})
 
