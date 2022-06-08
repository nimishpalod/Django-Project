from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is Home")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse(" We are My Library")

def contact(request):
    return render(request, 'contact.html')
