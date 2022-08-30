from urllib import request
from django.shortcuts import render
import random

def home(request):
    p = random.randrange(1,10)
    s = random.randrange(1,10)
    sp = {
        'love' : 'Matching' if p==s else 'Not Matching',
        'R' : p,
        'A' : s
    }
    return render(request,'index.html',sp)


def link(request):
    return render(request,'subtem/link.html')



def action(request):
    return render(request,"subtem/dropdown/action.html")
    
    
    
