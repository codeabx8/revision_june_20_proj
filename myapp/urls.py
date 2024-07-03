from django.urls import path
from .views import home, portfolio,test, root_page,learning_context,using_bootstrap

urlpatterns =[
    path("", root_page,name="root_page"),
    path("portfolio/", portfolio,name="portfolio"),
    path("learning-context/",learning_context,name="learning_context"),
    path("using_boostrap/", using_bootstrap, name="u_boots"),
    path("test/",test,name="test"),
    path("", home),
 ]