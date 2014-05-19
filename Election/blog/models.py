#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.db.models import permalink
class BlogPost(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    timestamp=models.DateTimeField()
    class Meta:
        ordering=('-timestamp',)
    def __unicode__(self):
        return self.title
    @permalink
    def get_absolute_url(self):
        return ('blog_view',[str(self.id)])
class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','timestamp')
admin.site.register(BlogPost,BlogPostAdmin)
