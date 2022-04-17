from django.shortcuts import render
from django.http import HttpResponse
from . models import Student

# Create your views here.
def home(request):

    students = Student.objects.all()

    params = {"students": students}

    return render(request, "deployApp/index.html", params)