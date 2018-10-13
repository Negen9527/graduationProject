from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.


class Project(models.Model):
    p_title = models.CharField(max_length=64)
    p_content = UEditorField(width=600, height=800)
    p_read_count = models.IntegerField(default=0)
    p_datetime = models.DateTimeField(auto_now=True)
    p_language = models.CharField(max_length=32)
    is_delete = models.BooleanField(default=False)


