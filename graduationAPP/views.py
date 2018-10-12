from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.


def index(request):
    content = ''
    project = Project.objects.get(pk=1)
    content = project.pinfo
    return render(request, 'graduationApp/index.html', {"content":content})


def detail(request):
    title = ''
    pinfo = ''
    project = Project.objects.get(pk=1)
    ptitle = project.ptitle
    pinfo = project.pinfo
    ret_data = {
        'title': ptitle,
        'content': pinfo
    }
    return render(request, 'graduationApp/detail.html', ret_data)