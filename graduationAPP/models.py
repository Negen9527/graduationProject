from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.


class Project(models.Model):
    ptitle = models.CharField(max_length=64)
    pinfo = UEditorField(width=600, height=800)
    pread_count = models.IntegerField(default=0)
    pdatetime = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)


