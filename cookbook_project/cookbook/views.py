# DJANGO IMPORTS
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# COOKBOOK IMPORTS
from cookbook.models import Category, Recipe, Comment, Ingredient, Rating
from cookbook.forms import UserForm, IngredientForm, RecipeForm, CommentForm
# HAYSTACK IMPORTS
#from haystack.query import SearchQuerySet


#-HELPER-FUNCTIONS------------------------------------------------------

def username_check(request):
    username = None
    available = None
    if request.method == 'GET':
        username = request.GET['username']

        if username:
            users = User.objects.filter(username=username)
            if len(users) > 0:
                available = False
            else:
                available = True

    return HttpResponse(available)
    


@login_required
def rate_recipe(request):
    recipe_id = None
    value = None
    rating  = None
    if request.method == 'GET':
        recipe_id = request.GET['recipe_id']
        recipe = Recipe.objects.get(id=recipe_id)
        value = request.GET['value']

        if recipe and value:
            rating = recipe.rate(request.user, int(value))

    return HttpResponse(rating)


@login_required
def delete_recipe(request):
    recipe_id = None
    deleted = False
    if request.method == 'GET':
        recipe_id = request.GET['recipe_id']
        recipe = Recipe.objects.get(id=recipe_id)

        if recipe and recipe.user == request.user:
            recipe.delete()
            deleted = True

    return HttpResponse(deleted)
            

@login_required
def delete_comment(request):
    comment_id = None
    deleted = False
    if request.method == 'GET':
        comment_id = request.GET['comment_id']
        comment = Comment.objects.get(id=comment_id)

        if comment and request.user == comment.user:
            comment.delete()
            deleted = True

    return HttpResponse(deleted)
            

@login_required
def save_recipe(request):
    recipe_user = None
    recipe_slug = None
    saved = None
    
    if request.method == 'GET':
        # get the recipe author and recipe slug
        recipe_user = User.objects.get(username=request.GET['user'])
        recipe_slug = request.GET['slug']
            
        # if request contains both
        if recipe_user and recipe_slug:
            # try and get a recipe object
            recipe = Recipe.objects.get(user=recipe_user, slug=recipe_slug)

            # if the recipe object exists
            if recipe:
                # either save or unsave the recipe and set saved to new value
                if recipe not in Recipe.objects.filter(saved_by=request.user):
                    recipe.user_save(request.user)
                    saved = True
                else:
                    recipe.user_unsave(request.user)
                    saved = False
    return HttpResponse(saved)        


#-HOME-SECTION----------------------------------------------------------

def home(request):
    context_dict = {}
    best_rated = Recipe.objects.order_by('-total_rating')[:5]
    new_recipes = Recipe.objects.order_by('-upload_date')[:5]
    context_dict['best_rated'] = best_rated
    context_dict['new_recipes'] = new_recipes
    
    response = render(request, 'cookbook/home.html', context_dict)
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
    
    return render(request, 'cookbook/signup.html', context_dict)

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
                # login the user and redirect to their profile
                login(request, user)
                return HttpResponseRedirect(reverse('cookbook:myprofile'))

            # inactive account
            else:
                context_dict['errors'] = ['Your CookBook account is disabled.']
                return render(request, 'cookbook/user_login.html', context_dict)

        # invalid login details
        else:
            print('Invalid login details: {0}, {1}'.format(username, password))
            context_dict['errors'] = ['Invalid login details']
            return render(request, 'cookbook/user_login.html', context_dict)
        
    else:
        # Not HTTP POST
        return render(request, 'cookbook/user_login.html', context_dict)

@login_required
def user_logout(request):
    # logout user and redirect to home page
    logout(request)
    return HttpResponseRedirect(reverse('cookbook:home'))

@login_required
def myprofile(request):
    context_dict = {}
        
    recipes = Recipe.objects.filter(user=request.user)
    if recipes:
        recipe = recipes.order_by('-upload_date')

    recent_comments = Comment.objects.filter(recipe__in=recipes)
    if recent_comments:
        recent_comments = recent_comments.order_by('-upload_date')[:10]
    
    context_dict['recent_comments'] = recent_comments
    context_dict['recipes'] = recipes

    return render(request, 'cookbook/myprofile.html', context_dict)

@login_required
def savedrecipes(request):
    context_dict = {}

    saved_recipes = Recipe.objects.filter(saved_by=request.user)[::-1]
    context_dict['saved_recipes'] = saved_recipes
    
    return render(request, 'cookbook/saved_recipes.html', context_dict)

@login_required
def uploadrecipe(request):
    context_dict = {}
    recipe_form = RecipeForm()
    if request.method == 'POST':
        # check if form is valid
        recipe_form = RecipeForm(request.POST, request.FILES)
        
        if recipe_form.is_valid():
            # create
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            
            if recipe.is_vegan or (recipe.is_vegetarian and recipe.is_dairy_free):
                recipe.is_vegan = True
                recipe.is_vegetarian = True
                recipe.is_dairy_free = True
            
            recipe.save()
            return view_recipe(request, request.user.username, recipe.name)
        
        else:
            print(recipe_form.errors)

    context_dict['recipe_form'] = RecipeForm()
    return render(request, 'cookbook/upload-recipe.html', context_dict)

# view for a user profile
def view_user(request, user):
    context_dict = {}

    try:
        user = User.objects.get(username=user)
        if user == request.user:
            return HttpResponseRedirect(reverse('cookbook:myprofile'))
            
        recipes = Recipe.objects.filter(user=user)

        context_dict['author'] = user
        context_dict['recipes'] = recipes

    except User.DoesNotExist:
        context_dict['author'] = None
        context_dict['recipes'] = None
    
    return render(request, 'cookbook/view_user.html', context_dict)

# Actual recipe view
def view_recipe(request, user, recipe_slug):
    context_dict = {}

    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.user = request.user
            comment.recipe = Recipe.objects.get(user=User.objects.get(username=user), slug=recipe_slug)
            comment.save()

            return HttpResponseRedirect(reverse('cookbook:view_recipe', args=[user, recipe_slug]))
    
    else:
        #HTTP GET so show the recipe
        
        try:
            # get the recipe
            user = User.objects.get(username=user)
            recipe = Recipe.objects.get(user=user, slug=recipe_slug)
            if request.user != user:
                recipe.views += 1
                recipe.save()

            # get the recipes ingredients
            ingredients = Ingredient.objects.filter(recipe=recipe)

            # get the recipes comments
            comments = Comment.objects.filter(recipe=recipe).order_by('-upload_date')

            if request.user.is_authenticated():
                saved = recipe in Recipe.objects.filter(saved_by=request.user)
                if request.user != recipe.user:
                    my_rating = Rating.objects.filter(user=request.user, recipe=recipe)
                    if len(my_rating) > 0:
                        rating = my_rating[0].value
                    else:
                        rating = None
                else:
                    rating = None
            else:
                saved = None
                rating = None
            
            context_dict['recipe'] = recipe
            context_dict['ingredients'] = ingredients
            context_dict['comments'] = comments
            context_dict['saved'] = saved
            context_dict['commentForm'] = CommentForm()
            context_dict['rating'] = rating

        except (User.DoesNotExist, Recipe.DoesNotExist):
            context_dict['recipe'] = None
            context_dict['ingredients'] = None
            context_dict['comments'] = None
            context_dict['saved'] = None
            context_dict['commentForm'] = None
            context_dict['rating'] = None

             
        return render(request, 'cookbook/view_recipe.html', context_dict)



#-CATEGORY-SECTION--(finding-recipes)--------------------------------------

def categories(request):
    context_dict = {}
    categories = Category.objects.all()
    context_dict['categories'] = categories
    
    return render(request, 'cookbook/categories.html', context_dict)

# for all categories
def view_category(request, category_name):
    context_dict = {}
    try:
        category = Category.objects.get(name=category_name)
        recipes = Recipe.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['recipes'] = recipes

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['recipes'] = None
    
    return render(request, 'cookbook/view_category.html', context_dict)

def bestrated(request):
    context_dict = {}
    recipes = Recipe.objects.order_by('-total_rating')
    context_dict['recipes'] = recipes
    return render(request, 'cookbook/best_rated.html', context_dict)
	
def newestrecipes(request):
    context_dict = {}
    recipes = Recipe.objects.order_by('-upload_date')
    context_dict['recipes'] = recipes
    return render(request, 'cookbook/newest_recipes.html', context_dict)

# search only for article names
def search(request):
    context_dict = {}
    if request.method == "GET":
        search_text = request.GET.get('search_box', None)
    else:
        return render(request, 'search/search.html', context_dict)
    if search_text == "":
        return render(request, 'search/search.html', context_dict)	
    recipes = Recipe.objects.filter(name__contains=search_text)
    context_dict['recipes'] = recipes
    return render(request, 'search/search.html', context_dict)
    #return HttpResponse('search')

#-HELP-SECTION------------------------------------------------------------

def about(request):
    return render(request, 'cookbook/help.html')

def faq(request):
    return render(request, 'cookbook/faq.html')

def conversioncharts(request):
    return render(request, "cookbook/conversion-charts.html")

def recipeguide(request):
    return render(request, 'cookbook/recipeguide.html')

def commentingrules(request):
    return render(request, 'cookbook/commenting-rules.html')
