from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#function based
#def Home(request):
    #if(request.method=="GET"):
        #return HttpResponse("Welcome To Django")
# define index view returns message "index page"
#def Index(request):
  #  if(request.method=="GET"):
   #     return HttpResponse("Index page")
# CLASS BASED
from django.views import View
class Home(View):
    def get(self,request):
        return HttpResponse("welcome to django")

class Index(View):
    def get(self,request):
        return HttpResponse("Index")