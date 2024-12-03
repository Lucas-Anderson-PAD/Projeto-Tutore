from django.shortcuts import render, request

# Create your views here.
def home():
    return render(request, "home.html")