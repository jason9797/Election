#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django import forms
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import loader, Context
from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import Count
import json
# Create your views here.
from models import *
from forms import *
def create_election(request):
    username=request.user
    if username.id is None:
        response=HttpResponse()
        response.write("<script language='javascript'>alert('请先登录!');window.location.href='../../login';</script>")
        return response
    form =ElectionForm(request.POST,request.FILES or None)
    response_info=[]
    if form.is_valid():
        data = form.cleaned_data
        name=data['name']
        job=data['job']
        if len(Election.objects.filter(name=name).filter(job=job))==0:
            form.save()
            response=HttpResponse()
            response.write("<script language='javascript'>alert('竞选成功!');window.location.href='../../homepage';</script>")
            return response
        else:
            #response_info.append('输入信息有误或者你已竞选过该职位')
            response=HttpResponse()
            response.write("<script language='javascript'>alert('输入信息有错或者你已竞选过该职位!');window.location.href='../../election/create';</script>")
            return response
    form=ElectionForm()
    return render_to_response('create_election.html',{'User':username,'form':form,'response_info':response_info})
    #t=get_template('create_election.html')
    #c = RequestContext(request,{'form':form,'response_info':response_info})
    #return HttpResponse(t.render(c))

def electioninfo(request,id):
    username=request.user
    if username.id is None:
        response=HttpResponse()
        response.write("<script language='javascript'>alert('请先登录!');window.location.href='../../login';</script>")
        return response
    posts=Election.objects.filter(pk=id)
    username=User.objects.get(username=request.user)
    t = loader.get_template("election_info.html")
    c = Context({ 'posts': posts ,'User':username})
    return HttpResponse(t.render(c))
def vote_result(request):
    username=request.user
    right=User.objects.filter(username=username)
    if username.id is None:
        response=HttpResponse()
        response.write("<script language='javascript'>alert('请先登录!');window.location.href='../../login';</script>")
        return response
    if len(right.filter(is_staff=1))==0:
        response=HttpResponse()
        response.write("<script language='javascript'>alert('你没有权限!');window.location.href='../../homepage';</script>")
        return response
    username=User.objects.get(username=request.user)
    t=loader.get_template('vote_result.html')
    c=Context({'User':username})
    return HttpResponse(t.render(c))
def vote_ajax_info(request):
    response=HttpResponse()
    user=request.GET.get('user')
    job=request.GET.get('job')
    name=request.GET.get('name')
    ret='0'
    if len(Vote.objects.filter(vote_man=user).filter(vote_job=job))!=0:
        ret=1
    else:
        vote_info=Vote(vote_man=user,votes=1,vote_job=job,vote_to_man=name)
        vote_info.save()
        ret=2
    response['Content-Type']="text/javascript"
    response.write(ret)
    return response
def ajax_get_result(request):
     response=HttpResponse()
     user=request.GET.get('user')
     job=request.GET.get('job')
     #result_info=list(Election.objects.filter(job=job))+list(Vote.objects.filter(vote_job=job))
     result_info=[]
     election_job=Election.objects.filter(job=job)
     for i in range(len(election_job)):
         vote_quality=Vote.objects.filter(vote_job=job,vote_to_man=election_job[i].name).count()
         result_info.append({'name':election_job[i].name,'img':election_job[i].photo.name,'no':vote_quality})
         result_info=sorted(result_info,key=lambda x:x['no'],reverse=True)
         #result_info.append([election_job[i].name,election_job[i].photo.name,vote_quality])
         #result_info=sorted(result_info,key=lambda x:x[2],reverse=
     result_info=json.dumps(result_info)
     response.write(result_info)
     return response

    
