from .forms import NameForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
import requests


def index(request):
    url="https://api.openweathermap.org/data/2.5/weather?appid=7fb043e5ad2c1a712cfed8e74dc27bcb&q={}"
    city="india"
    r=requests.get(url.format(city)).json()
    city_del={
        "city":city,
        "discription":r["weather"][0]["description"],
        "temperature":r["main"]["temp"],
        "icon":r["weather"][0]["icon"]}
    print(city_del)


    return render(request,'weatherindex.html',{'weather':city_del})
def cityinfo(request):
    if request.method=='POST':
        cityname=NameForm(request.POST)
    else:
        cityname=NameForm()
    return render(request,"weather2.html",{"weather":cityname})
    
