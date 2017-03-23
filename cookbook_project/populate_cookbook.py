# -*- coding: cp1252 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cookbook_project.settings')

import django
django.setup()
from cookbook.models import Recipe, Comment, Category, Rating
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
        # TOFU CURRY
        {'user': 'HummusLover123',
         'category': 'Mains',
         'name': 'Tofu Curry',
         'picture': os.path.join('recipe_images', 'HummusLover123', 'tofu-curry.jpg'),
         'description': "Curried tofu made with coconut milk.",
         'ingredients': """500g tofu,
                        pinch of salt,
                        20g butter,
                        2 onions,
                        clove of garlic,
                        1/4 pint of coconut milk,
                        2 tbsp curry powder""",
         'method': """1. Heat oil in a large skillet over medium-high heat. Add tofu cubes, 
                         season with seasoned salt and fry until golden on all sides, stirring occasionally
                         , about 15 minutes. Remove to paper towels, and set aside 
                         2. Melt butter or margarine in the same skillet over medium heat. Add the onion and garlic; 
                         cook and stir until tender. Stir in coconut milk, curry powder, salt, 
                         pepper and cilantro. Return the tofu to the skillet. Simmer over low 
                         heat for 15 minutes, stirring occasionally.""",
         'serves': 4,
         'spice': 2,
         'cooking_time': 60,
         'is_vegetarian': True,
         'is_vegan': True,
         'is_gluten_free': False,
         'is_dairy_free': True},
        # ROAST BEEF
        {'user': 'HealthyDad',
         'category': 'Mains',
         'name': 'Roast Beef',
         'picture': os.path.join('recipe_images', 'HealthyDad', 'roast-beef.jpg'),
         'description': "A simple way to roast topside of beef to ensure it's super succulent, every time.",
         'ingredients': """14oz beef,
                        mixed vegetables,
                        100g gravy granules""",
         'method': """Drizzle the beef with oil and season well with sea salt 
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
        # GREEN SMOOTHIE
        {'user': 'HummusLover123',
         'category': 'Drinks',
         'name': 'Green Smoothie',
         'picture': os.path.join('recipe_images', 'HummusLover123', 'green-smoothie.jpg'),
         'description': "A sweet smoothie with nutricious ingredients.",
         'ingredients': """250ml almond milk,
                        small banana,
                        1 tbsp ground flaxseed,
                        a pinch of cinnamon,
                        a handful of spinach,
                        1 tbsp almond butter""",
         'method': """Pour the milk into a high-speed blender then add the ground 
                         flaxseed and the cinnamon. Add the remaining ingredients then 
                         blitz until smooth. Pour into glasses and serve.""",
         'serves': 1,
         'spice': 0,
         'cooking_time': 5,
         'is_vegetarian': True,
         'is_vegan': True,
         'is_gluten_free': False,
         'is_dairy_free': True},
        # SWEET POTATO AND CARROT SOUP
        {'user': 'MaggiesMeals',
         'category': 'Starters',
         'name': 'Sweet Potato and Carrot Soup',
         'picture': os.path.join('recipe_images', 'MaggiesMeals', 'sweet-potato-and-carrot-soup.jpg'),
         'description': "Silky smooth soup, perfect for a dinner party.",
         'ingredients': """500g sweet potato,
                        300g carrot,
                        3 tbsp olive oil,
                        2 onions,
                        1 large vegetable stock,
                        100ml creme fraiche,
                        2 garlic cloves""",
         'method': """Heat oven to 220C and put sweet potato and carrots into large
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
        # WONDERFUL APPLE PIE
        {'user': 'CookingGranny',
         'category': 'Desserts',
         'name': 'Wonderful Apple Pie',
         'picture': os.path.join('recipe_images', 'CookingGranny', 'wonderful-apple-pie.jpg'),
         'description': "A traditional apple pie that the whole family is sure to love.",
         'ingredients': """1kg cooking apples,
                        140g caster sugar,
                        1/2 tbsp cinnamon,
                        3 tbsp flour (for filling),
                        225g butter,
                        2 eggs,
                        350g flour (for pastry)""",
         'method': """Slice apples and lay on a large baking sheet. Beat butter and sugar
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
        # WOO WOO
        {'user': 'MaggiesMeals',
         'category': 'Drinks',
         'name': 'Woo Woo',
         'picture': os.path.join('recipe_images', 'MaggiesMeals', 'woo-woo.jpg'),
         'description': "Fun and fruity!",
         'ingredients': """1 ounce vodka,
                        1 ounce peach schnapps,
                        2 ounces cranberry juice,
                        lime wedge for garnish""",   
         'method': """Place all ingredients into a cocktail shaker with ice. Shake well
                         and strain into a chilled glass with fresh ice. Garnish with a lime wedge.""",
         'serves': 1,
         'spice': 0,
         'cooking_time': 3,
         'is_vegetarian': True,
         'is_vegan': True,
         'is_gluten_free': True,
         'is_dairy_free': True},
        # CHEESE AND HAM OMELETTE (CookingGranny)
        {'user': 'CookingGranny',
         'category': 'Lunches',
         'name': 'Cheese and Ham Omelette',
         'picture': os.path.join('recipe_images', 'CookingGranny', 'cheese-and-ham-omelette.jpg'),
         'description': "A classic omelette recipe for one. Quick, easy, and super tasty!",
         'ingredients': """3 eggs,
                        10g unsalted butter,
                        30g Cheddar cheese,
                        1 slice of ham, chopped,
                        salt and black pepper""",
         'method': """Gently beat eggs together in a bowl and season with salt and pepper.
                         Heat the butter in a frying pan until foaming. Pour in eggs and cook for
                         a few seconds until the bottom of the omelette is lightly set. Push the
                         set parts of the omelette to the uncooked centre and cook again. Repeat
                         this process until the eggs have set but the omelette is still soft in
                         the centre. Put the cheese and three-quarters of the ham in the center
                         of the omelette and cook until the cheese melts. Increase the heat to high
                         and cook for 30 seconds, or until brown on the bottom. Fold the omelette
                         in half and then remove the pan from the heat. Put the omelette onto a
                         plate and sprinkle with the remaining ham.""",
         'serves': 1,
         'spice': 0,
         'cooking_time': 10,
         'is_vegetarian': False,
         'is_vegan': False,
         'is_gluten_free': True,
         'is_dairy_free': False},
        # CHEESE AND BACON SANDWICH
        {'user': 'BaconIsBest',
         'category': 'Lunches',
         'name': 'Cheese and Bacon Sandwich',
         'picture': os.path.join('recipe_images', 'BaconIsBest', 'cheese-and-bacon-sandwich.jpg'),
         'description': "Fantastic cheese and bacon sandwich. Truly the best!",
         'ingredients': """8 slices bacon,
                        1 onion,
                        4 slices cheddar cheese,
                        4 slices mozzarella cheese,
                        8 slices bread""",   
         'method': """Heat grill for 5 minutes. Grill bacon until browned, drain on
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
        # CURRIED VEGETABLE PIE
        {'user': 'HealthyDad',
         'category': 'Mains',
         'name': 'Curried Vegetable Pie',
         'picture': os.path.join('recipe_images', 'HealthyDad', 'curried-vegetable-pie.jpg'),
         'description': "A tasty vegetable pie with a spicy kick.",
         'ingredients': """2 tbsp sunflower oil,
                        1 onion,
                        2 garlic cloves,
                        1 green chilli,
                        1 tbsp garam masala,
                        1 tsp ground cumin,
                        2 carrots,
                        1 parsnip,
                        225g courgette,
                        75g peas,
                        25g butter,
                        25g plain flour,
                        4 tbsp Greek-style yoghurt,
                        3 tbsp corriander,
                        shortcrust pasrty (enough to cover pie),
                        1 tbsp milk""",
         'method': """Heat oven to 200C. Heat oil in large pan and cook onion, garlic
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
        # HUMBLE PIE
        {'user': 'BaconIsBest',
         'category': 'Drinks',
         'name': 'Humble Pie',
         'picture': os.path.join('recipe_images', 'BaconIsBest', 'humble-pie.jpg'),
         'description': "A refreshing orange cocktail.",
         'ingredients': """lots of ice,
                        40ml blood orange vodka,
                        20ml Aperol,
                        dash of lemonjuice,
                        soda water,
                        1 lemon wheel""",
         'method': """Fill a cocktail shaker with ice. Add blood orange vodka, Aperol,
                         and lemon juice. Shake until cold. Strain into an ice-filled glass
                         and top off with soda. Garnish with lemon wheel and serve.""",
         'serves': 1,
         'spice': 0,
         'cooking_time': 3,
         'is_vegetarian': True,
         'is_vegan': True,
         'is_gluten_free': True,
         'is_dairy_free': True},
        # SEAFOOD STEW
        {'user': 'MrFish',
         'category': 'Mains',
         'name': 'Seafood Stew',
         'picture': os.path.join('recipe_images', 'MrFish', 'seafood-stew.jpg'),
         'description': "All of your favourite fish in one fantastic dish.",
         'ingredients': """1 tbsp olive oil,
                        1 onion,
                        1 garlic clove,
                        1 1/2 tbsp paprika,
                        400g tinned chopped tomatoes,
                        600ml chicken stock,
                        450g skinless white fish fillets,
                        175g peeled king prawns,
                        200g mussles""",
         'method': """Heat oil in a pan with a lid. Add onion and cook until softened. Stir
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
        # CHEESE AND HAM OMELETTE (MaggiesMeals)
        {'user': 'MaggiesMeals',
         'category': 'Lunches',
         'name': 'Cheese and Ham Omelette',
         'picture': os.path.join('recipe_images', 'MaggiesMeals', 'cheese-and-ham-omelette.jpg'),
         'description': "A simple omelette that makes for a quick, cheap lunch.",
         'ingredients': """2 eggs,
                        25g Cheddar cheese,
                        salt and ground pepper,
                        1 tsp olive oil,
                        1 slice of cooked ham,
                        sprig of fresh thyme""",
         'method': """Beat egg yolks together with cheese and season with salt and pepper.
                         Whisk egg whites until just stiff and fold into the egg yolk mixture. Heat
                         the oil in a small non-stick pan and add the omelette mix. Cook until
                         golden underneath, and scatter with chopped ham. Place pan under a
                         pre-heated grill until the omelette starts to rise and is set. Slide onto
                         a plate, fold in half and serve with thyme.""",
         'serves': 1,
         'spice': 0,
         'cooking_time': 10,
         'is_vegetarian': False,
         'is_vegan': False,
         'is_gluten_free': True,
         'is_dairy_free': False},
    ]

    comments = [
        # TOFU CURRY
        {'username': 'MaggiesMeals',
         'recipe_author': 'HummusLover123',
         'recipe_name': 'Tofu Curry',
         'text': 'love it!'},
        {'username': 'BaconIsBest',
         'recipe_author': 'HummusLover123',
         'recipe_name': 'Tofu Curry',
         'text': 'How to improve: 1. Put tofu in bin 2. Buy meat'},
        # ROAST BEEF
        {'username': 'HummusLover123',
         'recipe_author': 'HealthyDad',
         'recipe_name': 'Roast Beef',
         'text': 'eww meat'},
        {'username': 'MaggiesMeals',
         'recipe_author': 'HealthyDad',
         'recipe_name': 'Roast Beef',
         'text': 'Yummy!'},
        {'username': 'BaconIsBest',
         'recipe_author': 'HealthyDad',
         'recipe_name': 'Roast Beef',
         'text': 'I think it would be better without the veg. Meat is great though!'},
        # GREEN SMOOTHIE
        {'username': 'HealthyDad',
         'recipe_author': 'HummusLover123',
         'recipe_name': 'Green Smoothie',
         'text': 'The kids did not enjoy this one...'},
        # SWEET POTATO AND CARROT SOUP 
        {'username': 'HummusLover123',
         'recipe_author': 'MaggiesMeals',
         'recipe_name': 'Sweet Potato and Carrot Soup',
         'text': 'I made this without the creme fraiche and it was simply divine!'},
        # WONDERFUL APPLE PIE
        {'username': 'HealthyDad',
         'recipe_author': 'CookingGranny',
         'recipe_name': 'Wonderful Apple Pie',
         'text': 'Superb!'},
        {'username': 'MaggiesMeals',
         'recipe_author': 'CookingGranny',
         'recipe_name': 'Wonderful Apple Pie',
         'text': 'Absolutely fantastic!'},
        # CHEESE AND BACON SANDWICH
        {'username': 'HealthyDad',
         'recipe_author': 'BaconIsBest',
         'recipe_name': 'Cheese and Bacon Sandwich',
         'text': 'My girls love them!'},
        # CURRIED VEGETABLE PIE
        {'username': 'CookingGranny',
         'recipe_author': 'HealthyDad',
         'recipe_name': 'Curried Vegetable Pie',
         'text': 'Keeps me warm through the winter. Really tasty.'},
        {'username': 'BaconIsBest',
         'recipe_author': 'HealthyDad',
         'recipe_name': 'Curried Vegetable Pie',
         'text': 'Interesting recipe, but no meat?'},
        # HUMBLE PIE
        {'username': 'MaggiesMeals',
         'recipe_author': 'BaconIsBest',
         'recipe_name': 'Humble Pie',
         'text': 'Great! My friends all love it!'},
        {'username': 'CookingGranny',
         'recipe_author': 'BaconIsBest',
         'recipe_name': 'Humble Pie',
         'text': 'Fantastic!'},
        # CHEESE AND HAM OMELETTE (CookingGranny)
        {'username': 'MaggiesMeals',
         'recipe_author': 'CookingGranny',
         'recipe_name': 'Cheese and Ham Omelette',
         'text': 'I really like this recipe; a classic!'},
    ]

    ratings = [
        # TOFU CURRY
        {'username': 'HealthyDad',
         'recipe_slug': 'tofu-curry',
         'recipe_author': 'HummusLover123',
         'value': 4},
        {'username': 'MaggiesMeals',
         'recipe_slug': 'tofu-curry',
         'recipe_author': 'HummusLover123',
         'value': 5},
        {'username': 'BaconIsBest',
         'recipe_slug': 'tofu-curry',
         'recipe_author': 'HummusLover123',
         'value': 1},
        {'username': 'MrFish',
         'recipe_slug': 'tofu-curry',
         'recipe_author': 'HummusLover123',
         'value': 4},
		 {'username': 'CookingGranny',
         'recipe_slug': 'tofu-curry',
         'recipe_author': 'HummusLover123',
         'value': 4},
        # ROAST BEEF
        {'username': 'HummusLover123',
         'recipe_slug': 'roast-beef',
         'recipe_author': 'HealthyDad',
         'value': 1},
        {'username': 'MaggiesMeals',
         'recipe_slug': 'roast-beef',
         'recipe_author': 'HealthyDad',
         'value': 4},
        {'username': 'BaconIsBest',
         'recipe_slug': 'roast-beef',
         'recipe_author': 'HealthyDad',
         'value': 5},
        # GREEN SMOOTHIE
        {'username': 'HealthyDad',
         'recipe_slug': 'green-smoothie',
         'recipe_author': 'HummusLover123',
         'value': 1},
        {'username': 'CookingGranny',
         'recipe_slug': 'green-smoothie',
         'recipe_author': 'HummusLover123',
         'value': 1},
        {'username': 'MrFish',
         'recipe_slug': 'green-smoothie',
         'recipe_author': 'HummusLover123',
         'value': 2},
        # SWEET POTATO AND CARROT SOUP
        {'username': 'HummusLover123',
         'recipe_slug': 'sweet-potato-and-carrot-soup',
         'recipe_author': 'MaggiesMeals',
         'value': 5},
        {'username': 'CookingGranny',
         'recipe_slug': 'sweet-potato-and-carrot-soup',
         'recipe_author': 'MaggiesMeals',
         'value': 4},
        # WONDERFUL APPLE PIE
        {'username': 'HealthyDad',
         'recipe_slug': 'wonderful-apple-pie',
         'recipe_author': 'CookingGranny',
         'value': 5},
        {'username': 'MrFish',
         'recipe_slug': 'wonderful-apple-pie',
         'recipe_author': 'CookingGranny',
         'value': 5},
        {'username': 'MaggiesMeals',
         'recipe_slug': 'wonderful-apple-pie',
         'recipe_author': 'CookingGranny',
         'value': 5},
        {'username': 'BaconIsBest',
         'recipe_slug': 'wonderful-apple-pie',
         'recipe_author': 'CookingGranny',
         'value': 5},
        # CHEESE AND BACON SANDWICH
        {'username': 'HealthyDad',
         'recipe_slug': 'cheese-and-bacon-sandwich',
         'recipe_author': 'BaconIsBest',
         'value': 4},
        {'username': 'MaggiesMeals',
         'recipe_slug': 'cheese-and-bacon-sandwich',
         'recipe_author': 'BaconIsBest',
         'value': 3},
        # CURRIED VEGETABLE PIE
        {'username': 'CookingGranny',
         'recipe_slug': 'curried-vegetable-pie',
         'recipe_author': 'HealthyDad',
         'value': 5},
		{'username': 'BaconIsBest',
         'recipe_slug': 'curried-vegetable-pie',
         'recipe_author': 'HealthyDad',
         'value': 2},
        {'username': 'MaggiesMeals',
         'recipe_slug': 'curried-vegetable-pie',
         'recipe_author': 'HealthyDad',
         'value': 4},
        {'username': 'MrFish',
         'recipe_slug': 'curried-vegetable-pie',
         'recipe_author': 'HealthyDad',
         'value': 3},
        # HUMBLE PIE
        {'username': 'MaggiesMeals',
         'recipe_slug': 'humble-pie',
         'recipe_author': 'BaconIsBest',
         'value': 5},
        {'username': 'MrFish',
         'recipe_slug': 'humble-pie',
         'recipe_author': 'BaconIsBest',
         'value': 3},
        # SEAFOOD STEW
        {'username': 'HealthyDad',
         'recipe_slug': 'seafood-stew',
         'recipe_author': 'MrFish',
         'value': 3},
        # CHEESE AND HAM OMELETTE (CookingGranny)
        {'username': 'MaggiesMeals',
         'recipe_slug': 'cheese-and-ham-omelette',
         'recipe_author': 'CookingGranny',
         'value': 4},
        # WOO WOO
        {'username': 'BaconIsBest',
         'recipe_slug': 'woo-woo',
         'recipe_author': 'MaggiesMeals',
         'value': 5},
        {'username': 'CookingGranny',
         'recipe_slug': 'woo-woo',
         'recipe_author': 'MaggiesMeals',
         'value': 3},
        {'username': 'MrFish',
         'recipe_slug': 'woo-woo',
         'recipe_author': 'MaggiesMeals',
         'value': 3},
    ]

    for user in users:
        add_user(user['username'], user['email'], user['password'])

    for cat in categories:
        add_category(cat['name'], cat['picture'])

    for rec in recipes:
        add_recipe(rec['user'], rec['category'],rec['name'], rec['picture'],
                   rec['description'], rec['ingredients'], rec['method'],
                   rec['serves'], rec['spice'], rec['cooking_time'],
                   rec['is_vegetarian'],
                   rec['is_vegan'], rec['is_gluten_free'], rec['is_dairy_free'])

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
            print("- {0} - {1} - {2} ({3}) - {4} comments".format(str(u), str(r), r.total_rating, r.no_of_ratings, len(Comment.objects.filter(recipe=r))))

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


if __name__ == '__main__':
    print("Starting CookBook population script...")
    populate()

    

        
