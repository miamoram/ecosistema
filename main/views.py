from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Space
import folium
from  folium.plugins import FastMarkerCluster


def home(request):
    return render(request, "index.html")

@login_required
def dashboard(request):
    m = folium.Map(location=[4.6404919,-74.1322655], zoom_start=9)
    try:
        spaces = Space.objects.filter(enable=1).order_by('name')                
        latitudes = [space.lat for space in spaces]
        longitudes = [space.long for space in spaces]
        FastMarkerCluster(data=list(zip(latitudes,longitudes))).add_to(m)
        """for space in spaces:
            coordinates = (space.lat, space.long)
            folium.Marker(coordinates).add_to(m)        """
    except Space.DoesNotExist:
        print("No se tienen espacios registradas")
    finally:
        return render(request, "dashboard.html", {"map": m._repr_html_()})

def signup(request):
    if (request.method == 'GET'):
        return render(request, "signup.html")
    else:
        if (request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("/dashboard")
            except: 
                return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": "El usuario ya existe"
                })
        else:
            return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": "Las contraseñas no coinciden"
                })

def signout(request):
    logout(request)
    return redirect("home")

def signin(request):
    if (request.method == 'GET'):
        return render(request, "signin.html", {
            "form": AuthenticationForm
        })
    else:    
        user = authenticate(request, username= request.POST["username"], password = request.POST["password"])
        if user is None:
          return render(request, "signin.html", {
            "form": AuthenticationForm,
            "error": "Usuario o Password no validos"
        })
        else:
            login(request, user)
            return redirect("dashboard")

