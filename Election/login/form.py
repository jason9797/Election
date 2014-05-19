#-*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名')
    email = forms.EmailField(label='邮箱地址')
    password = forms.CharField(label='密码',widget=forms.PasswordInput)
    password2= forms.CharField(label='再输一次',widget=forms.PasswordInput)
    def pwd_validate(self,p1,p2):
        return p1==p2
    
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码',widget=forms.PasswordInput)
    captcha=CaptchaField()
class ChangepwdForm(forms.Form):
    old_pwd = forms.CharField(label='旧密码',widget=forms.PasswordInput)
    new_pwd = forms.CharField(label='新密码',widget=forms.PasswordInput)
    new_pwd2= forms.CharField(label='再输一次',widget=forms.PasswordInput)    
