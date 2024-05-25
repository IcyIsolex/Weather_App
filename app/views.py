from django.shortcuts import render
from .forms import userinput
from .models import City
import requests
import json
def index(request):
    url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=66bed5563a4ee8777844060903e85d05'
    if request.method=='POST':
        form=userinput(request.POST)
        form.save()
    form=userinput()
    cityinput=City.objects.all()
    var_a=[]
    for i in cityinput:
        a=requests.get(url.format(i)).json()
        my_dict={ "city":i.cityname,
            "Temperature":round(a["main"]["temp"]-273.15),
            "Description":a["weather"][0]["description"],
            "Icon":a["weather"][0]["icon"]} 
        var_a.append(my_dict)
    

    my_dict2={"City_Weather":var_a,
            "form":form
            }
    return render(request,"app/app.html",my_dict2)

# Create your views here.
