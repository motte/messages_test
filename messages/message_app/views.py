from django.shortcuts import render
from django.views.generic import ListView

class StateMessageView(ListView):
    
    def __init__(self, *args, **kwargs):

        super(StateMessageView,self).__init__(self, *args, **kwargs)

