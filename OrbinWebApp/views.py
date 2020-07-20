from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "OrbinWebApp/home.html")

def servicios(request):
    return render(request, "OrbinWebApp/servicios.html")

def portfolio(request):
    return render(request, "OrbinWebApp/portfolio.html")

def blog(request):
    return render(request, "OrbinWebApp/blog.html")

def contacto(request):
    return render(request, "OrbinWebApp/contacto.html")