from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"projectnewapp/home.html")

def about(request):
    return render(request,"projectnewapp/about.html")

def store(request):
    return render(request,"projectnewapp/store.html")