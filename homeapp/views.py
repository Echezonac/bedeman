from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    context={
        "Carousels":Carousel.objects.all(),
        "cvs":CV.objects.all(),
        "archprojects":ArchProject.objects.all().order_by('-date'),
        "techprojects":TechProject.objects.all().order_by('-date'),
        "bisprojects":BisProject.objects.all().order_by('-date'),
    }
    return render(request,'main/index.html',context)
