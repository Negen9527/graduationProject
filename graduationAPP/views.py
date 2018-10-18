from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from django.core.paginator import Paginator
# Create your views here.
from .utils import *


def index(request):
    currentpage = request.GET.get('page')
    if currentpage is None:
        currentpage = 1
    else:
        currentpage = int(currentpage)
    rows = 10
    projects = Project.objects.all()[(currentpage-1)*rows: currentpage*rows]
    nums = range(0, 10-len(projects))
    contacts = listing(Project, 10, currentpage)
    hotProjects = getHotProjects()
    result_data = {"projects": projects,
                   "nums": nums,
                   "contacts": contacts,
                   "hotProjects": hotProjects}

    return render(request, 'graduationApp/index.html', result_data)


def detail(request):
    projectId = request.GET.get('projectId')
    index(request)
    title = ''
    pcontent = ''
    project = Project.objects.get(pk=projectId)
    project.p_read_count += 1
    project.save()
    ptitle = project.p_title
    pcontent = project.p_content
    hotProjects = getHotProjects()
    ret_data = {
        'title': ptitle,
        'content': pcontent,
        'read_count': project.p_read_count,
        'hotProjects': hotProjects,
    }
    return render(request, 'graduationApp/detail.html', ret_data)


def search(request):
    currentpage = request.GET.get('page')
    if currentpage is None:
        currentpage = 1
    else:
        currentpage = int(currentpage)
    keyword = request.GET.get('keyword')
    result_projects = Project.objects.filter(p_title__contains=keyword)

    nums = range(0, 10-len(result_projects))
    contacts = listing(Project, 10, currentpage)
    hotProjects = getHotProjects()
    result_data = {"projects": result_projects,
                   "nums": nums,
                   "contacts": contacts,
                   "hotProjects": hotProjects}
    return render(request, 'graduationApp/searchResult.html', result_data)
