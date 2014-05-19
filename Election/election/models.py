#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.db.models import permalink

JOB_CHOICES=(
    (u'班长','班长'),
    (u'副班长','副班长'),
    (u'团支书','团支书'),
    (u'学习委员','学习委员'),
    (u'文艺委员','文艺委员'),
    (u'体育委员','体育委员'),
    (u'生活委员','生活委员'),
    )
class Election(models.Model):
    name=models.CharField('姓名',max_length=100)
    number=models.IntegerField('学号')
    Class=models.CharField('班级',max_length=250)
    job=models.CharField('竞选职务',max_length=250,choices=JOB_CHOICES)
    reason=models.TextField('竞选原因')
    video=models.URLField('竞选视频',max_length=250)
    photo=models.ImageField('上传图片',upload_to='photos')
class Vote(models.Model):
    vote_man=models.CharField('投票人',max_length=250)
    votes=models.IntegerField('一票')
    vote_job=models.CharField('职务',max_length=250)
    vote_to_man=models.CharField('投给谁',max_length=250)
