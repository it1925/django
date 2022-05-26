from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_show(request):
    x = []
    for i in range(10):
        x.append(i)
    return HttpResponse("Loaded")