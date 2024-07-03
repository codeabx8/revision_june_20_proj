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
def test(request):
    return render(request, template_name="myapp/test.html")

def root_page(request):
    return render(request,template_name="myapp/root_page.html")

def learning_context(request):
    student={"name":"Arun","age":20,"address":"ktm","email":"arun@gmail.com"}
    students=[
        {"name": "Arun", "age": 20, "address": "ktm", "email": "arun@gmail.com"},
        {"name": "Barun", "age": 22, "address": "ktm", "email": "run@gmail.com"},
        {"name": "Tarun", "age": 30, "address": "ktm", "email": "un@gmail.com"},
        {"name": "Sagar", "age": 19, "address": "ktm", "email": "sagar@gmail.com"},
    ]
    return render(request, template_name="myapp/learning_context.html",context={"students":students,"student":student})

def using_bootstrap(request):
    students =[
        {"name": "Arun", "age": 20, "address": "ktm", "email": "arun@gmail.com"},
        {"name": "Barun", "age": 22, "address": "ktm", "email": "run@gmail.com"},
        {"name": "Tarun", "age": 30, "address": "ktm", "email": "un@gmail.com"},
        {"name": "Sagar", "age": 19, "address": "ktm", "email": "sagar@gmail.com"},
    ]
    return render(request, template_name="myapp/using_bootstrap.html", context={"students":students})