from django.contrib import admin

# Register your models here.
from .models import *
class ProjectAdmin(admin.ModelAdmin):
    # list_display = ['id', 'pname', 'pinfo', 'pimage']
    pass

admin.site.register(Project, ProjectAdmin)

