from django.shortcuts import render

# Create your views here.
def student(request):
    return render(request, template_name="commons/student.html")