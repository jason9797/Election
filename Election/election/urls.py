#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from Election.election.views import *

urlpatterns = patterns('',
        url(r'create/$', create_election),
        url(r'info/(\d+)$',electioninfo),
        url(r'result/$',vote_result)
        
)

