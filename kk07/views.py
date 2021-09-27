from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    contact = {
    "variable1":"Rahul is great"
    "variable2": "Rohan is great"
    } 
    return render(request, 'index.html', context)

   # return HttpResponse("balaji")

def about(request):
    return HttpResponse("about")

def services(request):
    return HttpResponse("services")

def contact(request):
    return HttpResponse("contact")




