from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    d = {'author' : 'faisal', 'age' : 21 , 'lst' :['Bangladesh','is','my','motherland'],'birthdate': datetime.datetime.now(),
         'val' : ' ', 'value' : 6, 'name' : [
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
    ],
    }
    return render(request,'home.html',d)
