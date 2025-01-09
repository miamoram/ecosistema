import io
import os
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Residue, Trash_can
from main.models import Space
import requests
from PIL import Image
from django.conf import settings
from django.shortcuts import get_object_or_404


#@login_required
def index(request):
    context ={}
    data = []
    #result = []
    #TODO Consultar los datos del usuario autenticado
    context["trash_can"]= Trash_can.objects.filter(enable=1).filter(user_id=request.user.id).order_by('name')            
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for file in request.FILES.getlist('file'):            
                residue = Residue(photo=file)
                residue.url = residue.photo.path #TODO actualizar a url real
                residue.name = file.name
                try:
                    residue.trash_can = Trash_can.objects.get(pk=form.cleaned_data["trash_can"])
                except Trash_can.DoesNotExist:
                    print("Se guarda sin caneca")
                finally:                    
                    residue.save()                    
                    predict_img(residue)
                    predict_json(residue)
                    data.append(residue)                
            context ["data"]= data            
            #context ["result"] = result
    elif request.method == "GET":
        print("ToDO")    
    return render(request, "clasification.html", context= context )
    
from django.core.files import File


def predict_img(residue):

    endpoint = os.path.join(settings.API_CLASIFICACION, "object-to-img")    
    files = {
    'file': (os.path.join(settings.MEDIA_ROOT,residue.photo.name), open(os.path.join(settings.MEDIA_ROOT,residue.photo.name), 'rb')),
    'Content-Type': 'image/jpeg'    
    }
    response = requests.post(endpoint, files=files)
    #predicted = response.json()
    print ("status code " + str(response.status_code))
    if response.status_code == 200:
        print ("Success")
        with io.BytesIO(response.content) as f:
            with Image.open(f) as img:
                img.save(os.path.join(settings.MEDIA_ROOT,"img",str(residue.id)+"_predicted.jpg"))                
        with open(os.path.join(settings.MEDIA_ROOT,"img",str(residue.id)+"_predicted.jpg"), 'rb') as fi:
            residue.photo_predicted = File(fi, name=os.path.basename(fi.name))
            residue.save()
    else:
        print ("Failure")
    return residue

def predict_json(residue):

    endpoint = os.path.join(settings.API_CLASIFICACION, "object-to-json")    
    files = {
    'file': (os.path.join(settings.MEDIA_ROOT,residue.photo.name), open(os.path.join(settings.MEDIA_ROOT,residue.photo.name), 'rb')),
    'Content-Type': 'image/jpeg'    
    }
    response = requests.post(endpoint, files=files)
    print ("status code " + str(response.status_code))
    if response.status_code == 200:
        print ("Success")
        residue.predicted = response.json()
        residue.save()
    else:
        print ("Failure")
    return residue
