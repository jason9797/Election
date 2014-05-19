#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from form import RegisterForm,LoginForm,ChangepwdForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import serializers
import sys
sys.path.append('C:/Users/Administrator/Desktop/Election/Election')
from election.models import Election

# Create your views here.
def register(request):
    error=[]
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            email = data['email']
            password = data['password']
            password2= data['password2']
            if not User.objects.all().filter(username=username):
                if form.pwd_validate(password, password2):
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    login_validate(request,username,password)
                    return HttpResponseRedirect('/homepage/')
                else:
                    error.append('请输入相同的密码')
            else:
                error.append('用户名已存在，请换个用户名')
    else:
        form = RegisterForm()    
    return render_to_response('register.html',{'form':form,'error':error})
            
        
def login_validate(request,username,password):
    rtvalue = False
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            auth_login(request,user)
            return True
    return rtvalue
#def homepage(request):
    #return HttpResponse("Welcome to Homepage!")
def mylogin(request):
    error = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            human = True
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            
            if login_validate(request,username,password):
                #return render_to_response('welcome.html',{'user':username})
                return HttpResponseRedirect('/homepage/')
            else:
                error.append('密码错误')
        else:
            error.append('输入有错误')
    else:
        form = LoginForm()
    return render_to_response('login.html',{'error':error,'form':form})
def mylogout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')
def homepage(request):
    username=request.user
    if username.id is None:
        response=HttpResponse()
        response.write("<script language='javascript'>alert('请先登录!');window.location.href='../login';</script>")
        return response
    return render_to_response('welcome.html',{'user':username})
def changepassword(request,username):
    error = []
    if request.method == 'POST':
        form = ChangepwdForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=username,password=data['old_pwd'])
            if user is not None:
                if data['new_pwd']==data['new_pwd2']:
                    newuser = User.objects.get(username__exact=username)
                    newuser.set_password(data['new_pwd'])
                    newuser.save()
                    return HttpResponseRedirect('/login/')
                else:
                    error.append('请输入相同的密码')
            else:
                error.append('请输入正确的旧密码')
        else:
            error.append('请按照规则输入')
    else:
        form = ChangepwdForm()
    return render_to_response('changepassword.html',{'form':form,'error':error})
def ajax_get_json(request):
    response=HttpResponse()
    job=request.GET.get('job')
    response['Content-Type']="text/javascript"
    response.write(serializers.serialize("json",Election.objects.filter(job=job)))
    return response
    
