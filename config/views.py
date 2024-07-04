from django.shortcuts import render, redirect

def index(request):
    return render(request,"index.html")

def videos(request):
    return render(request,"videos.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def detail(request):
    return render(request,"photo-detail.html")