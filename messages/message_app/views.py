from django.shortcuts import render
from django.core import serializers
import simplejson
from django.views.generic import CreateView, ListView
from django.http import HttpResponse

class PostMessageView(CreateView):
    template_name = 'index.html'


    def post(self, request, *args, **kwargs):

        super(PostMessageView, self).post(self)


class StatMessageView(ListView):

    def get(self, request, *args, **kwargs):

        data = serializers.serialize('json', stat_queryset)
        return HttpResponse(data, mimetype='application/json')