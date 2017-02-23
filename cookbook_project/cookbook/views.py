from django.shortcuts import render
from django.http import HttpResponse

#-HOME-SECTION----------------------------------------------------------

def home(request):
    # placeholder home view
    return HttpResponse("This is the home")

#-USER-SECTION----------------------------------------------------------

def signup(request):
    return HttpResponse("sign up here")

def login(request):
    return HttpResponse("login")

def myprofile(request):
    return HttpResponse("my profileplaceholder")

def savedrecipes(request):
    return HttpResponse("saved recipes")

def uploadrecipe(request):
    return HttpResponse("upload recipe")

# view for a user profile
def view_user(request):
    return HttpResponse("view someone elses profile")

# Actual recipe view
def view_recipe(request):
    return HttpResponse("view a recipe")



#-CATEGORY-SECTION--(finding recipes)--------------------------------------

def categories(request):
    return HttpResponse("view all categories")

# for all categhories
def view_category(request):
    return HttpResponse("specific category")

def bestrated(request):
    return HttpResponse("best rated recipes here")

# search and search results
def search(request):
    return HttpResponse("search for recipes")

#-HELP-SECTION------------------------------------------------------------

def about(request):
    return HttpResponse("help page")

def faq(request):
    return HttpResponse("FAQ page")

def conversioncharts(request):
    return HttpResponse("helpful conversion charts")

def recipeguide(request):
    return HttpResponse("how to write a recipe")

def commentingrules(request):
    return HttpResponse("commenting and website rules")
