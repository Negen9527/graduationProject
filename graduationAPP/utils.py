#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Time    : 2018/10/13 13:40
@Author  : Negen
@Site    : 
@File    : utils.py
@Software: PyCharm
'''
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from graduationAPP.models import Project


def listing(model_name, page_size, currentpage):
    model_list = model_name.objects.all()
    paginator = Paginator(model_list, page_size)
    # page = request.GET.get('page')
    page = currentpage
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return contacts


def getHotProjects():
    projects = Project.objects.all().order_by('-p_read_count')
    if projects.__len__() > 5:
        return projects[0:5]
    else:
        return projects

