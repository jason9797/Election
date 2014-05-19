#-*- coding: utf-8 -*-
from django import forms
from models import *
class ElectionForm(forms.ModelForm):
    class Meta:
        model=Election
    def __init__(self,*args, **kwargs):
        super(ElectionForm, self).__init__(*args, **kwargs)

class VoteForm(forms.ModelForm):

    class Meta:
        model=Vote
admin.site.register(Election)
admin.site.register(Vote)