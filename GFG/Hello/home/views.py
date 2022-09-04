from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("HomePage")
    return render(request,"index.html")


def team(request):
    return render(request,"team.html")

def events(request):
    return render(request,"events.html")