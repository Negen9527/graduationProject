from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    后台自定义显示
    """
    list_display = ['id', 'p_title', 'p_language', 'p_datetime']

# admin.site.register(Project, ProjectAdmin)

