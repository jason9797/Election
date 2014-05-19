#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from Election.blog.views import archive

urlpatterns = patterns('',
        url(r'^(\d+)/$', archive,name='blog_view'),
        #url(r'^(?P<title>\w+)/$',archive,name='blog_view')
)

