from django.shortcuts import render
from django.http import HttpResponse
from .models import QNA,sanQNA

# Create your views here.
def home(request):
    return render(request, 'home.html')

def rashmi(request):
    
    return render(request, 'rashmi.html')  
    

def sandesh(request):
    
    return render(request, 'sandesh.html')

def submitras(request):
    name = request.POST.get('name')
    relation = request.POST.get('relation') 
    question = request.POST.get('question')
    option1 = request.POST.get('option1')
    option2 = request.POST.get('option2')
    option3 = request.POST.get('option3')
    option4 = request.POST.get('option4')

    data=QNA(name=name,relation=relation, question=question, option1=option1, option2=option2, option3=option3, option4=option4)
    data.save()
    return render(request, 'submit.html')
def submitsan(request):
    name = request.POST.get('name')
    relation = request.POST.get('relation') 
    question = request.POST.get('question')
    option1 = request.POST.get('option1')
    option2 = request.POST.get('option2')
    option3 = request.POST.get('option3')
    option4 = request.POST.get('option4')

    data1=sanQNA(name=name,relation=relation, question=question, option1=option1, option2=option2, option3=option3, option4=option4)
    data1.save()
    return render(request, 'submit.html')

