from django.db import models
from django.contrib.auth.models import User


#Zonas geograficas en donde se agrupan los espacios
class Zone(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

#Espacios en donde se encuentran las canecas de basura
class Space(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    enable = models.BooleanField(default=True)
    long = models.DecimalField(max_digits=9, decimal_places=8)
    lat = models.DecimalField(max_digits=9, decimal_places=8)
    zone = models.ForeignKey(Zone, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

#Canecas de basura    
class Trash_can(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    enable = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    space = models.ForeignKey(Space, on_delete=models.DO_NOTHING, default=None)    

    def __str__(self):
        return self.name + ' - ' + self.space.name
