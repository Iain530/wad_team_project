from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from cookbook.models import Category, Recipe, Comment

#-HOME-SECTION----------------------------------------------------------

def home(request):
    context_dict = {}
    best_rated = Recipes.objects.order_by('-rating')[:5]
    new_recipes = Recipes.objects.order_by('-upload_date')[:5]
    context_dict['best_rated'] = best_rated
    context_dict['new_recipes'] = new_recipes
    #when template is made
    #response = render(request, 'cookbook/home.html', context_dict)
    response = HttpResponse("This is the home")
    return response

#-USER-SECTION----------------------------------------------------------

def signup(request):
    #to do
    return HttpResponse("sign up here")

def login(request):
    #to do
    return HttpResponse("login")

@login_required
def myprofile(request):
    context_dict = {}
    
    recent_comments = Comments.objects.filter(user=request.user).order_by(['-upload_date'])[:10]
    recipes = Recipes.objects.filter(user=request.user).order_by(['-upload_date'])

    context_dict['recent_comments'] = recent_comments
    context_dict['recipes'] = recipes

    return HttpResponse("my profile")

@login_required
def savedrecipes(request):
    context_dict = {}
    #to do
    return HttpResponse("saved recipes")

@login_required
def uploadrecipe(request):
    #to do
    return HttpResponse("upload recipe")

# view for a user profile
def view_user(request, user):
    context_dict = {}

    try:
        user = User.objects.get(username=user)
        recipes = Recipe.objects.filter(user=user)

        context_dict['recipes'] = recipes

    except User.DoesNotExist:
        context_dict['recipes'] = None
    
    return HttpResponse("view someone elses profile")

# Actual recipe view
def view_recipe(request, user, name):
    context_dict = {}

    try:
        recipe = Recipe.objects.get(user=user, name=name)
        context_dict['recipe'] = recipe

    except Recipe.DoesNotExist:
        context_dict['recipe'] = None
    
    return HttpResponse("view a recipe")


#-CATEGORY-SECTION--(finding recipes)--------------------------------------

def categories(request):
    context_dict = {}
    categories = Category.objects
    cotext_dict['categories'] = categories
    
    return HttpResponse("view all categories")

# for all categhories
def view_category(request, category):
    context_dict = {}

    recipes = Recipe.objects.filter(category=category)
    context_dict['recipes'] = recipes
    
    return HttpResponse("specific category")

def bestrated(request):
    context_dict = {}
    recipes = Recipes.objects.order_by('-rating')
    context_dict['recipes'] = recipes
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
