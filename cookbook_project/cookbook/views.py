# DJANGO IMPORTS
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# COOKBOOK IMPORTS
from cookbook.models import Category, Recipe, Comment, Ingredient
from cookbook.forms import UserForm, CategoryForm, IngredientForm

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
    registered = False

    if request.method == 'POST':
        # check if form is valid
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # create user
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            # invalid form/errors, print to terminal
            print(user_form.errors)

    else:
        # create blank form
        user_form = UserForm()

    context_dict = {}
    context_dict['user_form'] = user_form
    context_dict['registered'] = registered
    
    return HttpResponse("sign up here")

def user_login(request):
    context_dict = {}

    if request.method == 'POST':
        # check if username and password are valid
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            # check account is not disabled
            if user.is_active:
                # login the user
                login(request, user)
                return HttpResponseRedirect(reverse('myprofile'))
            else:
                # inactive account
                context_dict['errors'] = ['Your CookBook account is disabled.']
                #return render(request, LOGIN HTML, context_dict)
                return HttpResponse('disabled account')
        else:
            # invalid login details
            print('Invalid login details: {0}, {1}'.format(username, password))
            context_dict['errors'] = ['Invalid login details']
            #return render(request, LOGIN HTML, context_dict)
            return HttpResponse('Invalid login details')
        
    else:
        # Not HTTP POST
        #return render(request, LOGIN HTML, context_dict)
        return HttpResponse('login here')

@login_required
def user_logout(request):
    # logout user and redirect to home page
    logout(request)
    return HttpResponRedirect(reverse('home'))

@login_required
def myprofile(request):
    context_dict = {}
    
    recent_comments = Comments.objects.filter(user=request.user).order_by(['-upload_date'])[:10]
    recipes = list(Recipes.objects.filter(user=request.user).order_by(['-upload_date']))

    context_dict['recent_comments'] = recent_comments
    context_dict['recipes'] = recipes

    return HttpResponse("my profile")

@login_required
def savedrecipes(request):
    context_dict = {}

    saved_recipes = Recipe.objects.filter(saved_by__user=request.user)
    context_dict['saved_recipes'] = saved_recipes
    # to do
    return HttpResponse("saved recipes")

@login_required
def uploadrecipe(request):
    context_dict = {}
    
    if request.method == 'POST':
        # check if form is valid
        recipe_form = RecipeForm(request.POST)
        
        if form.is_valid():
            # create
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user

            if recipe.is_vegan or (recipe.is_vegetarian and recipe.is_dairy_free):
                recipe.is_vegan = True
                recipe.is_vegetarian = True
                recipe.is_dairy_free = True

            recipe.save()
            return view_recipe(request, request.user, recipe.name)

        else:
            print(form.errors)

    context_dict['form'] = RecipeForm()
    #return render(request, UPLOAD HTML, context_dict)    
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

    if request.method == 'GET':

        try:
            # get the recipe
            recipe = Recipe.objects.get(user=user, name=name)
            recipe.views += 1

            # get the recipes ingredients
            ingredients = Ingredients.objects.filter(recipe=recipe)

            # get the recipes comments
            comments = Comments.objects.filter(recipe=recipe).order_by('-upload_date')
            
            context_dict['recipe'] = recipe
            context_dict['ingredients'] = ingredients
            context_dict['comments'] = comments

        except Recipe.DoesNotExist:
            context_dict['recipe'] = None
            context_dict['ingredients'] = None
            context_dict['comments'] = None
             
        return HttpResponse("view a recipe")

    else:
        # HTTP POST (posting a comment/rating)
        return HttpResponse("comment/rating posted")


#-CATEGORY-SECTION--(finding-recipes)--------------------------------------

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
