from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
#
#
# def index(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())

from django.http import HttpResponse
from django.template import loader
from .models import Members


def index(request):
    members = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'members': members,
    }
    return HttpResponse(template.render(context, request))
