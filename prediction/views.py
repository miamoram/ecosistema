import io
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from urllib3 import encode_multipart_formdata
import urllib3
import shutil
from .forms import UploadFileForm
from .models import Residue
import requests
from io import StringIO
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
                data.append(residue)
                result.append(predict(residue.photo.path))
            context ["data"]= data            
            context ["result"] = result
    elif request.method == "GET":
        data = []    
    return render(request, "clasification.html", context= context )

def predict(url):    
    endpoint = "http://127.0.0.1:8001/object-to-img"
    files = {
    'file': (url, open( url, 'rb')),
    'Content-Type': 'image/jpeg'    
    }
    response = requests.post(endpoint, files=files)
    #predicted = response.json()
    print ("status code " + str(response.status_code))
    if response.status_code == 200:
        print ("Success")
        with io.BytesIO(response.content) as f:
            with Image.open(f) as img:
                img.save(settings.STATIC_ROOT+("/predicted.jpg"))
        """with open(static("predict.jpg"), 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)        
        print (response)"""
    else:
        print ("Failure")
    print(type(img))
    return "/predicted.jpg"
    
