from django.urls import path
from .views import home, portfolio,test, root_page,learning_context

urlpatterns =[
    path("", root_page,name="root_page"),
    path("portfolio/", portfolio,name="portfolio"),
    path("learning-context/",learning_context,name="learning_context"),
    path("test/",test,name="test"),
    path("", home),
 ]