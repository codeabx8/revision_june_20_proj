from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    query_string=request.GET
    name=query_string.get("name")
    print(name)
    return HttpResponse(f"<h1>I am revision the django project again. I am also learning {name} </h1>")

def  portfolio(request):
    return render(request, template_name="myapp/portfolio.html")