from django.test import TestCase
from django.contrib.auth.models import User
# COOKBOOK IMPORTS
from cookbook.models import Category, Recipe, Comment, Rating
from cookbook.forms import UserForm, RecipeForm, CommentForm

# Create your tests here.









#Definitions to make life easier

def add_user(username, email, password):
    if not User.objects.filter(username=username):
        u = User.objects.get_or_create(username=username, email=email, password=password)[0]
        u.set_password(u.password)
        u.save()
        return u

def add_category(name, picture):
    c = Category.objects.get_or_create(name=name, picture=picture)[0]
    c.save()
    return c

def add_recipe(username, category, name, picture, description, ingredients,
               method, serves, spice, cooking_time,
               is_vegetarian, is_vegan, is_gluten_free, is_dairy_free):
    
    user = User.objects.get(username=username)
    cat = Category.objects.get(name=category)
        
    r = Recipe.objects.get_or_create(user=user, category=cat, name=name,
                                     picture=picture, description=description,
                                     ingredients=ingredients,
                                     method=method, serves=serves,
                                     spice=spice, cooking_time=cooking_time,
                                     is_vegetarian=is_vegetarian,
                                     is_vegan=is_vegan, is_gluten_free=is_gluten_free,
                                     is_dairy_free=is_dairy_free)[0]

    r.save()
    return r


def add_comment(username, recipe_name, recipe_author, text):
    user = User.objects.get(username=username)
    
    recipe_user = User.objects.get(username=recipe_author)
    recipe = Recipe.objects.get(name=recipe_name, user=recipe_user)

    c = Comment.objects.get_or_create(user=user, recipe=recipe, text=text)[0]
    c.save()
    return c