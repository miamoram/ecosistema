from django.urls import path


from . import views

urlpatterns = [
    path('clasifica', views.index, name="clasification.html")    
]
