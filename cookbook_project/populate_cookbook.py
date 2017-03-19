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
        {'user': 'HealthyDad',
         'category': 'Mains',
         'name': 'Curried Vegetable Pie',
         'picture': os.path.join('recipe_images', 'HealthyDad', 'curried-vegetable-pie.jpg'),
         'description': "A tasty vegetable pie with a spicy kick.",
         'instructions': """Heat oven to 200C. Heat oil in large pan and cook onion, garlic
                         and chilli until tender. Stir in garam masala, tumeric and cumin,
                         and cook for 2-3 mins. Add carrots, parsnip, cauliflower and courgette
                         to pan with 300ml water. Bring to boil and simmer until vegetables are
                         almost tender. Drain, reserving the cooking liquid, and mix with peas.
                         Melt butter into a small pan, stir in flour and cook for 1 min. Add
                         reserved cooking liquid and cook, stirring, until it forms a thick
                         sauce. Simmer for 3 mins, stirring, then remove fro heat and mix in
                         yoghurt, coriander, vegetables and seasoning. Leave to cool. Spoon
                         mixture into a 900ml pie dish and brush the rim with water. Roll out
                         pastry and use to cover pie, pressing firmly onto the rim. Trim edges
                         and make a small hole in centre to allow steam to escape. Brush with
                         milk and bake for 25-30 mins.""",
         'serves': 4,
         'spice': 2,
         'cooking_time': 75,
         'is_vegetarian': True,
         'is_vegan': False,
         'is_gluten_free': False,
         'is_dairy_free': False},
        {'user': 'BaconIsBest',
         'category': 'Drinks',
         'name': 'Humble Pie',
         'picture': os.path.join('recipe_images', 'BaconIsBest', 'humble-pie.jpg'),
         'description': "A refreshing orange cocktail.",
         'instructions': """Fill a cocktail shaker with ice. Add blood orange vodka, Aperol,
                         and lemon juice. Shake until cold. Strain into an ice-filled glass
                         and top off with soda. Garnish with lemon wheel and serve.""",
         'serves': 1,
         'spice': 0,
         'cooking_time': 3,
         'is_vegetarian': True,
         'is_vegan': True,
         'is_gluten_free': True,
         'is_dairy_free': True},
        {'user': 'MrFish',
         'category': 'Mains',
         'name': 'Seafood Stew',
         'picture': os.path.join('recipe_images', 'MrFish', 'seafood-stew.jpg'),
         'description': "All of your favourite fish in one fantastic dish.",
         'instructions': """Heat oil in a pan with a lid. Add onion and cook until softened. Stir
                         in garlic and paprika, cook for 2 mins, then pour in tomatoes and stock.
                         Season, bring to boil, and reduce to a simmer for 10 mins. Add fish and
                         continue to cook for 2 mins. And prawns and mussels, then cover and cook
                         for another 3 mins. Discard any mussels that haven't opened and serve.""",
         'serves': 4,
         'spice': 0,
         'cooking_time': 30,
         'is_vegetarian': False,
         'is_vegan': False,
         'is_gluten_free': True,
         'is_dairy_free': True},
        {'user': 'MaggiesMeals',
         'category': 'Lunches',
         'name': 'Cheese and Ham Omelette',
         'picture': os.path.join('recipe_images', 'MaggiesMeals', 'cheese-and-ham-omelette.jpg'),
         'description': "A simple omelette that makes for a quick, cheap lunch.",
         'instructions': """Beat egg yolks together with cheese and season with salt and pepper.
                         Whisk egg whites until just stiff and fold into the egg yolk mixture. Heat
                         the oil in a small non-stick pan and add the omelette mix. Cook until
                         golden underneath, and scatter with chopped ham. Place pan under a
                         pre-heated grill until the omelette starts to rise and is set. Slide onto
                         a plate, fold in half and serve.""",
         'serves': 1,
         'spice': 0,
         'cooking_time': 10,
         'is_vegetarian': False,
         'is_vegan': False,
         'is_gluten_free': True,
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
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'sunflower oil',
         'quantity': '2 tbsp'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'onion',
         'quantity': '1'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'garlic clove',
         'quantity': '2'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'green chili',
         'quantity': '1'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'garam masala',
         'quantity': '1 tbsp'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'tumeric',
         'quantity': '1 tsp'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'ground cumin',
         'quantity': '1 tsp'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'carrot',
         'quantity': '2'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'parsnip',
         'quantity': '1'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'cauliflower floret',
         'quantity': '225g'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'courgette',
         'quantity': '1'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'peas',
         'quantity': '75g'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'butter',
         'quantity': '25g'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'plain flour',
         'quantity': '25g'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'Greek-style yoghurt',
         'quantity': '4 tbsp'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'coriander',
         'quantity': '3 tbsp'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'shortcrust pastry',
         'quantity': 'enough to cover pie'},
        {'recipe_name': 'Curried Vegetable Pie',
         'recipe_author': 'HealthyDad',
         'name': 'milk',
         'quantity': '1 tbsp'},
        {'recipe_name': 'Humble Pie',
         'recipe_author': 'BaconIsBest',
         'name': 'ice',
         'quantity': 'lots'},
        {'recipe_name': 'Humble Pie',
         'recipe_author': 'BaconIsBest',
         'name': 'blood orange vodka',
         'quantity': '1 ounce'},
        {'recipe_name': 'Humble Pie',
         'recipe_author': 'BaconIsBest',
         'name': 'Aperol',
         'quantity': '1 once'},
        {'recipe_name': 'Humble Pie',
         'recipe_author': 'BaconIsBest',
         'name': 'lemon juice',
         'quantity': '1/4 once'},
        {'recipe_name': 'Humble Pie',
         'recipe_author': 'BaconIsBest',
         'name': 'soda water',
         'quantity': 'enough to top off glass'},
        {'recipe_name': 'Humble Pie',
         'recipe_author': 'BaconIsBest',
         'name': 'lemon wheel',
         'quantity': '1'},
        {'recipe_name': 'Seafood Stew',
         'recipe_author': 'MrFish',
         'name': 'olive oil',
         'quantity': '1 tbsp'},
        {'recipe_name': 'Seafood Stew',
         'recipe_author': 'MrFish',
         'name': 'onion',
         'quantity': '1'},
        {'recipe_name': 'Seafood Stew',
         'recipe_author': 'MrFish',
         'name': 'garlic clove',
         'quantity': '1'},
        {'recipe_name': 'Seafood Stew',
         'recipe_author': 'MrFish',
         'name': 'paprika',
         'quantity': '1 1/2 tsp'},
        {'recipe_name': 'Seafood Stew',
         'recipe_author': 'MrFish',
         'name': 'tinned chopped tomatoes',
         'quantity': '400g'},
        {'recipe_name': 'Seafood Stew',
         'recipe_author': 'MrFish',
         'name': 'chicken stock',
         'quantity': '600ml'},
        {'recipe_name': 'Seafood Stew',
         'recipe_author': 'MrFish',
         'name': 'skinless white fish fillets',
         'quantity': '450g'},
        {'recipe_name': 'Seafood Stew',
         'recipe_author': 'MrFish',
         'name': 'peeled king prawns',
         'quantity': '175g'},
        {'recipe_name': 'Seafood Stew',
         'recipe_author': 'MrFish',
         'name': 'mussles',
         'quantity': '200g'},
        {'recipe_name': 'Cheese and Ham Omelette',
         'recipe_author': 'MaggiesMeals',
         'name': 'egg',
         'quantity': '2'},
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

    

        
