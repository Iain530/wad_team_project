import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cookbook_project.settings')

import django
django.setup()
from cookbook.models import Recipe, Ingredient, Comment, Category
from django.contrib.auth.models import User


def populate():

    users = [
        {'username': 'HummusLover123',
         'email': 'lesleyjones@hotmail.co.uk',
         'password': 'tofu4life'},
        {'username': 'HealthyDad',
         'email': 'adamsmith@gmail.com',
         'password': 'rachelsarah2824'},
        {'username': 'MaggiesMeals',
         'email': 'm_brown97@live.co.uk',
         'password': 'mealswithmaggie123'},
    ]

    categories = [
        {'name': 'Starters'},
        {'name': 'Mains'},
        {'name': 'Lunches'},
        {'name': 'Drinks'},
        {'name': 'Desserts'},
        {'name': 'Snacks'},
    ]

    recipes = [
        {'user': 'HummusLover123',
         'category': 'Mains',
         'name': 'Tofu Curry',
         'picture': 'recipe_images/tofu-curry.jpg',
         'instructions': 'intruction_intruction_intruction_\nintruction_\nintruction_',
         'serves': 4,
         'cooking_time': 60,
         'is_vegetarian': True,
         'is_vegan': True,
         'is_gluten_free': False,
         'is_dairy_free': True},
        {'user': 'HealthyDad',
         'category': 'Snacks',
         'name': 'Roast Beef',
         'picture': 'recipe_images/roast-beef.jpg',
         'instructions': 'intruction_intruction_intruction_\nintruction_\nintruction_',
         'serves': 3,
         'cooking_time': 90,
         'is_vegetarian': False,
         'is_vegan': False,
         'is_gluten_free': False,
         'is_dairy_free': False},
    ]

    ingredients = [
        {'recipe_name': 'Tofu Curry',
         'recipe_author': 'HummusLover123',
         'name': 'tofu',
         'quantity': '500g'},
        {'recipe_name': 'Tofu Curry',
         'recipe_author': 'HummusLover123',
         'name': 'salt',
         'quantity': 'pinch of'},
        {'recipe_name': 'Roast Beef',
         'recipe_author': 'HealthyDad',
         'name': 'beef',
         'quantity': '16oz'},
        {'recipe_name': 'Roast Beef',
         'recipe_author': 'HealthyDad',
         'name': 'salt',
         'quantity': 'big pinch'},
    ]

    comments = [
        {'username': 'MaggiesMeals',
         'recipe_author': 'HummusLover123',
         'recipe_name': 'Tofu Curry',
         'text': 'love it!'},
        {'username': 'HummusLover123',
         'recipe_author': 'HealthyDad',
         'recipe_name': 'Roast Beef',
         'text': 'eww meat'},
    ]

    ratings = [
        {'username': 'HummusLover123',
         'recipe_slug': 'roast-beef',
         'value': 1},
        {'username': 'MaggiesMeals',
         'recipe_slug': 'roast-beef',
         'value': 4},
        {'username': 'HealthyDad',
         'recipe_slug': 'tofu-curry',
         'value': 4},
        {'username': 'MaggiesMeals',
         'recipe_slug': 'tofu-curry',
         'value': 5},
    ]

    for user in users:
        add_user(user['username'], user['email'], user['password'])

    for cat in categories:
        add_category(cat['name'])

    for rec in recipes:
        add_recipe(rec['user'], rec['category'],rec['name'], rec['picture'],
                   rec['instructions'],
                   rec['serves'], rec['cooking_time'], rec['is_vegetarian'],
                   rec['is_vegan'], rec['is_gluten_free'], rec['is_dairy_free'])

    for ing in ingredients:
        add_ingredient(ing['recipe_name'], ing['recipe_author'], ing['name'],
                       ing['quantity'])

    for com in comments:
        add_comment(com['username'], com['recipe_name'], com['recipe_author'],
                    com['text'])

    # print users and their recipes
    for u in User.objects.all():
        for r in Recipe.objects.filter(user=u):
            print("- {0} - {1}".format(str(u), str(r)))

def add_user(username, email, password):
    u = User.objects.get_or_create(username=username, email=email, password=password)[0]
    u.set_password(u.password)
    u.save()
    return u

def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_recipe(username, category, name, picture, instructions, serves, cooking_time,
               is_vegetarian, is_vegan, is_gluten_free, is_dairy_free):
    
    user = User.objects.get(username=username)
    cat = Category.objects.get(name=category)
        
    r = Recipe.objects.get_or_create(user=user, category=cat, name=name,
                                     picture=picture,
                                     instructions=instructions, serves=serves,
                                     cooking_time=cooking_time,
                                     is_vegetarian=is_vegetarian,
                                     is_vegan=is_vegan, is_gluten_free=is_gluten_free,
                                     is_dairy_free=is_dairy_free)[0]

    r.save()
    return r

def add_ingredient(recipe_name, recipe_author, name, quantity):
    user = User.objects.get(username=recipe_author)
    recipe = Recipe.objects.get(user=user, name=recipe_name)

    i = Ingredient.objects.get_or_create(recipe=recipe, name=name, quantity=quantity)[0]
    i.save()
    return i

def add_comment(username, recipe_name, recipe_author, text):
    user = User.objects.get(username=username)
    
    recipe_user = User.objects.get(username=recipe_author)
    recipe = Recipe.objects.get(name=recipe_name, user=recipe_user)

    c = Comment.objects.get_or_create(user=user, recipe=recipe, text=text)[0]
    c.save()
    return c


if __name__ == '__main__':
    print("Starting CookBook population script...")
    populate()

    

        
