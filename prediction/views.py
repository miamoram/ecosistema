import io
import os
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Residue
import requests
from PIL import Image
from django.conf import settings

#@login_required
def index(request):
    context ={}
    data = []
    result = []
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for file in request.FILES.getlist('file'):            
                residue = Residue(photo=file)
                residue.url = residue.photo.path #TODO actualizar a url real
                residue.name = file.name
                residue.save()                    
                predict(residue)
                data.append(residue)                
            context ["data"]= data            
            context ["result"] = result
    elif request.method == "GET":
        data = []    
    return render(request, "clasification.html", context= context )
from django.core.files import File

def predict(residue):    
    #endpoint = "http://127.0.0.1:8001/object-to-img" #TODO url for path
    endpoint = "https://api-clasificacion.onrender.com"

    """with open("/home/miguel/proyectos/ecosistema/uploads/img/carton.jpeg", 'rb') as fi:
        residue.photo = File(fi, name=os.path.basename(fi.name))
        residue.save()"""
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
        """with open(static("predict.jpg"), 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)        
        print (response)"""
        with open(os.path.join(settings.MEDIA_ROOT,"img",str(residue.id)+"_predicted.jpg"), 'rb') as fi:
            residue.photo_predicted = File(fi, name=os.path.basename(fi.name))
            residue.save()
    else:
        print ("Failure")
    return residue
