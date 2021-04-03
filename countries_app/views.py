from django.shortcuts import render
import requests
from pprint import *
# Create your views here.


def index(request):
    
    return render(request,'index.html')



def list(request):
    url = "https://restcountries.eu/rest/v2/all"
        
    data = requests.get(url).json()
    pprint(data)
       
    return render(request,'list.html',{'data':data})

