# -*- coding: cp1252 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cookbook_project.settings')

import django
django.setup()
from cookbook.models import Recipe, Ingredient, Comment, Category, Rating
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
        {'username': 'BaconIsBest',
         'email': 'chrispbacon@hotmail.co.uk',
         'password': 'porkpower'},
        {'username': 'MrFish',
         'email': 'alanr70@gmail.com',
         'password': 'codtuna01'},
        {'username': 'CookingGranny',
         'email': 'debs22@yahoo.com',
         'password': '7grankids'},
    ]

    categories = [
        {'name': 'Starters',
         'picture': os.path.join('category_images', 'starters.jpg')},
        {'name': 'Mains',
         'picture': os.path.join('category_images', 'mains.jpg') },
        {'name': 'Lunches',
         'picture': os.path.join('category_images', 'lunches.jpg')},
        {'name': 'Drinks',
         'picture': os.path.join('category_images', 'drinks.jpg')},
        {'name': 'Desserts',
         'picture': os.path.join('category_images', 'desserts.jpg')},
        {'name': 'Snacks',
         'picture': os.path.join('category_images', 'snacks.jpg')},
    ]

    recipes = [
        {'user': 'HummusLover123',
         'category': 'Mains',
         'name': 'Tofu Curry',
         'picture': os.path.join('recipe_images', 'HummusLover123', 'tofu-curry.jpg'),
         'description': "Curried tofu made with coconut milk.",
         'instructions': """1. Heat oil in a large skillet over medium-high heat. Add tofu cubes, 
                         season with seasoned salt and fry until golden on all sides, stirring occasionally
                         , about 15 minutes. Remove to paper towels, and set aside 
                         2. Melt butter or margarine in the same skillet over medium heat. Add the onion and garlic; 
                         cook and stir until tender.Stir in coconut milk, curry powder, salt, 
                         pepper and cilantro. Return the tofu to the skillet. Simmer over low 
                         heat for 15 minutes, stirring occasionally.""",
         'serves': 4,
         'spice': 2,
         'cooking_time': 60,
         'is_vegetarian': True,
         'is_vegan': True,
         'is_gluten_free': False,
         'is_dairy_free': True},
        {'user': 'HealthyDad',
         'category': 'Snacks',
         'name': 'Roast Beef',
         'picture': os.path.join('recipe_images', 'HealthyDad', 'roast-beef.jpg'),
         'description': "A simple way to roast topside of beef to ensure it's super succulent, every time.",
         'instructions': """Drizzle the beef with oil and season well with sea salt 
                         and black pepper, then rub all over the meat. Place the beef on top of
                         the vegetables. Place the tray in the oven, then turn the heat down
                         immediately to 200 degrees C and cook for 1 hour for medium beef.""",
         'serves': 3,
         'spice': 0,
         'cooking_time': 90,
         'is_vegetarian': False,
         'is_vegan': False,
         'is_gluten_free': True,
         'is_dairy_free': True},
        {'user': 'HummusLover123',
         'category': 'Drinks',
         'name': 'Green Smoothie',
         'picture': os.path.join('recipe_images', 'HummusLover123', 'green-smoothie.jpg'),
         'description': "A sweet smoothie with nutricious ingredients.",
         'instructions': """Pour the milk into a high-speed blender then add the ground 
                         flaxseed and the cinnamon. Add the remaining ingredients then 
                         blitz until smooth. Pour into glasses and serve.""",
         'serves': 1,
         'spice': 0,
         'cooking_time': 5,
         'is_vegetarian': True,
         'is_vegan': True,
         'is_gluten_free': False,
         'is_dairy_free': True},
        {'user': 'MaggiesMeals',
         'category': 'Starters',
         'name': 'Sweet Potato and Carrot Soup',
         'picture': os.path.join('recipe_images', 'MaggiesMeals', 'sweet-potato-and-carrot-soup.jpg'),
         'description': "Silky smooth soup, perfect for a dinner party.",
         'instructions': """Heat oven to 220C and put sweet potato and carrots into large
                         roasting tin with seasoning and oil. Roast the veg for 25 mins til
                         tender. Fry the onion in a saucepan until soft and then add garlic.
                         Fry for 1 minute and then add stock. Simmer until onions very soft.
                         Once veg is done, transfer to pan an hand blend until smooth. Add
                         creme fraiche, seasoning, and then serve.""",
         'serves': 4,
         'spice': 0,
         'cooking_time': 50,
         'is_vegetarian': True,
         'is_vegan': False,
         'is_gluten_free': True,
         'is_dairy_free': False},
        {'user': 'CookingGranny',
         'category': 'Desserts',
         'name': 'Wonderful Apple Pie',
         'picture': os.path.join('recipe_images', 'CookingGranny', 'wonderful-apple-pie.jpg'),
         'description': "A traditional apple pie that the whole family is sure to love.",
         'instructions': """Slice apples and lay on a large baking sheet. Beat butter and sugar
                         into a large bowl. Break in a whole egg and a yolk (keep the white).
                         Beat this mix until it looks like scrambled egg. Work in flour for
                         pastry one third at a time until it begins to clump. Gently work this
                         dough into a ball and wrap it in cling film. Now mix sugar, cinnamon
                         and flour for filling into a bowl big enough for the apples. Heat oven
                         to 190C. Lighty beat egg whites. Cut off two thirds of the pastry and
                         roll it out, then use to line pie tin (20-22cm round, 4cm deep),
                         leaving a slight overhang. Roll out rest of pastry, ready to use as lid
                         of pie. Add apples to pie with cinnamon-sugar mix. Place lid on top
                         of pie, and pierce to allow steam to escape. Brush with egg whites
                         and bake for 40-45 mins.""",
         'serves': 8,
         'spice': 0,
         'cooking_time': 150,
         'is_vegetarian': True,
         'is_vegan': False,
         'is_gluten_free': False,
         'is_dairy_free': False},
        {'user': 'BaconIsBest',
         'category': 'Lunches',
         'name': 'Cheese and Bacon Sandwich',
         'picture': os.path.join('recipe_images', 'BaconIsBest', 'cheese-and-bacon-sandwich.jpg'),
         'description': "Fantastic cheese and bacon sandwich. Truly the best!",
         'instructions': """Heat grill for 5 minutes. Grill bacon until browned, drain on
                         papertowels and cut in half crosswise. Grill onion until tender.
                         Take bread and layer Cheddar cheese, bacon, onion, and mozzarella
                         cheese. Grill sandwiches until bread is toasted and cheese has
                         melted.""",
         'serves': 4,
         'spice': 0,
         'cooking_time': 25,
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
        {'recipe_name': 'Tofu Curry',
         'recipe_author': 'HummusLover123',
         'name': 'curry powder',
         'quantity': '2 tablespoons'},
        {'recipe_name': 'Tofu Curry',
         'recipe_author': 'HummusLover123',
         'name': 'chickpeas',
         'quantity': '200g'},
        {'recipe_name': 'Roast Beef',
         'recipe_author': 'HealthyDad',
         'name': 'beef',
         'quantity': '16oz'},
        {'recipe_name': 'Roast Beef',
         'recipe_author': 'HealthyDad',
         'name': 'salt',
         'quantity': 'big pinch'},
        {'recipe_name': 'Green Smoothie',
         'recipe_author': 'HummusLover123',
         'name': 'almond milk',
         'quantity': '250ml'},
        {'recipe_name': 'Green Smoothie',
         'recipe_author': 'HummusLover123',
         'name': 'banana',
         'quantity': 'a small one'},
        {'recipe_name': 'Green Smoothie',
         'recipe_author': 'HummusLover123',
         'name': 'ground flaxseed',
         'quantity': '1 tbsp'},
        {'recipe_name': 'Green Smoothie',
         'recipe_author': 'HummusLover123',
         'name': 'cinnamon',
         'quantity': 'a pinch'},
        {'recipe_name': 'Green Smoothie',
         'recipe_author': 'HummusLover123',
         'name': 'spinach',
         'quantity': 'a handful'},
        {'recipe_name': 'Green Smoothie',
         'recipe_author': 'HummusLover123',
         'name': 'almond butter',
         'quantity': '1 tbsp'},
        {'recipe_name': 'Sweet Potato and Carrot Soup',
         'recipe_author': 'MaggiesMeals',
         'name': 'sweet potato',
         'quantity': '500g'},
        {'recipe_name': 'Sweet Potato and Carrot Soup',
         'recipe_author': 'MaggiesMeals',
         'name': 'carrot',
         'quantity': '300g'},
        {'recipe_name': 'Sweet Potato and Carrot Soup',
         'recipe_author': 'MaggiesMeals',
         'name': 'olive oil',
         'quantity': '3 tbsp'},
        {'recipe_name': 'Sweet Potato and Carrot Soup',
         'recipe_author': 'MaggiesMeals',
         'name': 'onion',
         'quantity': '2'},
        {'recipe_name': 'Sweet Potato and Carrot Soup',
         'recipe_author': 'MaggiesMeals',
         'name': 'vegetable stock',
         'quantity': '1 large'},
        {'recipe_name': 'Sweet Potato and Carrot Soup',
         'recipe_author': 'MaggiesMeals',
         'name': 'creme fraiche',
         'quantity': '100ml'},
        {'recipe_name': 'Sweet Potato and Carrot Soup',
         'recipe_author': 'MaggiesMeals',
         'name': 'garlic cloves',
         'quantity': '2'},
        {'recipe_name': 'Wonderful Apple Pie',
         'recipe_author': 'CookingGranny',
         'name': 'cooking apples',
         'quantity': '1kg'},
        {'recipe_name': 'Wonderful Apple Pie',
         'recipe_author': 'CookingGranny',
         'name': 'caster sugar',
         'quantity': '140g'},
        {'recipe_name': 'Wonderful Apple Pie',
         'recipe_author': 'CookingGranny',
         'name': 'cinnamon',
         'quantity': '1/2 tsp'},
        {'recipe_name': 'Wonderful Apple Pie',
         'recipe_author': 'CookingGranny',
         'name': 'flour (for filling)',
         'quantity': '3 tbsp'},
        {'recipe_name': 'Wonderful Apple Pie',
         'recipe_author': 'CookingGranny',
         'name': 'butter',
         'quantity': '225g'},
        {'recipe_name': 'Wonderful Apple Pie',
         'recipe_author': 'CookingGranny',
         'name': 'egg',
         'quantity': '2'},
        {'recipe_name': 'Wonderful Apple Pie',
         'recipe_author': 'CookingGranny',
         'name': 'flour (for pastry)',
         'quantity': '350g'},
        {'recipe_name': 'Cheese and Bacon Sandwich',
         'recipe_author': 'BaconIsBest',
         'name': 'bacon',
         'quantity': '8 slices'},
        {'recipe_name': 'Cheese and Bacon Sandwich',
         'recipe_author': 'BaconIsBest',
         'name': 'bacon',
         'quantity': '8 slices'},
        {'recipe_name': 'Cheese and Bacon Sandwich',
         'recipe_author': 'BaconIsBest',
         'name': 'onion',
         'quantity': '1'},
        {'recipe_name': 'Cheese and Bacon Sandwich',
         'recipe_author': 'BaconIsBest',
         'name': 'Cheddar cheese',
         'quantity': '4 slices'},
        {'recipe_name': 'Cheese and Bacon Sandwich',
         'recipe_author': 'BaconIsBest',
         'name': 'mozzarella',
         'quantity': '4 slices'},
        {'recipe_name': 'Cheese and Bacon Sandwich',
         'recipe_author': 'BaconIsBest',
         'name': 'bread',
         'quantity': '8 slices'},
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
        {'username': 'MaggiesMeals',
         'recipe_author': 'HealthyDad',
         'recipe_name': 'Roast Beef',
         'text': 'Yummy!'},
        {'username': 'HealthyDad',
         'recipe_author': 'HummusLover123',
         'recipe_name': 'Green Smoothie',
         'text': 'The kids did not enjoy this one...'},
    ]

    ratings = [
        {'username': 'HummusLover123',
         'recipe_slug': 'roast-beef',
         'recipe_author': 'HealthyDad',
         'value': 1},
        {'username': 'MaggiesMeals',
         'recipe_slug': 'roast-beef',
         'recipe_author': 'HealthyDad',
         'value': 4},
        {'username': 'HealthyDad',
         'recipe_slug': 'tofu-curry',
         'recipe_author': 'HummusLover123',
         'value': 4},
        {'username': 'MaggiesMeals',
         'recipe_slug': 'tofu-curry',
         'recipe_author': 'HummusLover123',
         'value': 5},
        {'username': 'HealthyDad',
         'recipe_slug': 'green-smoothie',
         'recipe_author': 'HummusLover123',
         'value': 1},
    ]

    for user in users:
        add_user(user['username'], user['email'], user['password'])

    for cat in categories:
        add_category(cat['name'], cat['picture'])

    for rec in recipes:
        add_recipe(rec['user'], rec['category'],rec['name'], rec['picture'],
                   rec['description'], rec['instructions'],
                   rec['serves'], rec['spice'], rec['cooking_time'],
                   rec['is_vegetarian'],
                   rec['is_vegan'], rec['is_gluten_free'], rec['is_dairy_free'])

    for ing in ingredients:
        add_ingredient(ing['recipe_name'], ing['recipe_author'], ing['name'],
                       ing['quantity'])

    for com in comments:
        add_comment(com['username'], com['recipe_name'], com['recipe_author'],
                    com['text'])

    for rating in ratings:
        user = User.objects.get(username=rating['username'])
        recipe_author = User.objects.get(username=rating['recipe_author'])
        
        recipe = Recipe.objects.get(slug=rating['recipe_slug'], user=recipe_author)

        recipe.rate(user, rating['value'])

    # print users and their recipes
    for u in User.objects.all():
        for r in Recipe.objects.filter(user=u):
            print("- {0} - {1}".format(str(u), str(r)))

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

def add_recipe(username, category, name, picture, description, instructions, serves,
               spice, cooking_time,
               is_vegetarian, is_vegan, is_gluten_free, is_dairy_free):
    
    user = User.objects.get(username=username)
    cat = Category.objects.get(name=category)
        
    r = Recipe.objects.get_or_create(user=user, category=cat, name=name,
                                     picture=picture, description=description,
                                     instructions=instructions, serves=serves,
                                     spice=spice, cooking_time=cooking_time,
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

    

        
