from django.db import models
from main.models import Trash_can

# Residuos
class Residue(models.Model):
    url = models.URLField(null=False)
    name = models.CharField(max_length=80 )
    photo = models.ImageField(upload_to='static')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trash_can = models.ForeignKey(Trash_can, on_delete=models.DO_NOTHING, null=True)
    