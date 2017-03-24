from django.test import TestCase

from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
import os
from cookbook.models import Category, Recipe, Comment, Rating
from cookbook.forms import UserForm, RecipeForm, CommentForm, DeleteUserForm
from django.forms.models import model_to_dict
from django.contrib.staticfiles import finders
from django.template import loader
from django.conf import settings
from django.utils import timezone
#import test_utils
import populate_cookbook



#test cases for the homepage
class HomePageTests(TestCase):
	def test_home_using_template(self):
		response = self.client.get(reverse('cookbook:home'))
		self.assertTemplateUsed(response, 'cookbook/home.html')
		
	def test_home_has_title(self):
		# Check it has welcome message
		response = self.client.get(reverse('cookbook:home'))
		self.assertIn('Welcome to Cookbook'.lower(), response.content.lower())
		
	def test_does_home_contain_img(self):
		# Check if the home page contains an img
		response = self.client.get(reverse('cookbook:home'))
		self.assertIn('img', response.content)
	
	#TESTS WHEN NO RECIPES!!!
	def test_home_displays_no_newrecipes_message(self):
		# Access index with empty database
		response = self.client.get(reverse('cookbook:home'))
		# Check if no categories message is displayed
		self.assertIn("The newest recipes will appear here!", response.content)
	
	def test_home_displays_no_bestrated_recipes_message(self):
		# Access index with empty database
		response = self.client.get(reverse('cookbook:home'))
		# Check if no categories message is displayed
		self.assertIn("The best rated recipes will appear here!", response.content)
	 

#class MyProfileTest(TestCase):


#test cases for category page
class CategoryPageTests(TestCase):

    def test_index_context(self):
        # Access index with empty database
        response = self.client.get(reverse('cookbook:home'))

        
        populate_cookbook.populate()

        #Access index with database filled
        response = self.client.get(reverse('cookbook:home'))

        #Retrieve recipes from database by date
        recipes = Recipe.objects.order_by('-upload_date')[:2]
        #check newest recipes appear on the homepage
        for recipe in recipes:
	 			content = response.content.decode('utf-8')
	 			self.assertIn(recipe.name.lower(), content.lower())
	 	
	 	 #Retrieve recipes from database by rating
        recipes = Recipe.objects.filter(weighted_rating__gt=0).order_by('-weighted_rating')[:3]
        #check highest rating recipes appear on the homepage
        for recipe in recipes:
	 			content = response.content.decode('utf-8')
	 			self.assertIn(recipe.name.lower(), content.lower())
       


#test case for base html
class BaseHtmlTests(TestCase):

	 def test_base_template_exists(self):
	 	# Check base.html exists inside template folder
	 	path_to_base = settings.TEMPLATE_DIR + '/cookbook/base.html'
	 	print path_to_base
	 	self.assertTrue(os.path.isfile(path_to_base))
	 	
class TestCategories(TestCase):
	 #Test population script
	 def test_population_script_changes(self):


	 	#Populate database
	 	populate_cookbook.populate()
	 	# Check if the categories exist
		cat = Category.objects.get(name='Starters')
		cat = Category.objects.get(name='Desserts')
		cat = Category.objects.get(name='Lunches')
		cat = Category.objects.get(name='Snacks')		
		cat = Category.objects.get(name='Drinks')
		cat = Category.objects.get(name='Mains')
	

	 # For each category, access its page and check for the recipes associated with it
	 	categories = create_categories()
	 	for category in categories:
	 		cat = Category.objects.get(name=category)
	 		# Access category page
	 		response = self.client.get(reverse('cookbook:view_category', args=[cat]))
	 		#check category using template
	 		self.assertTemplateUsed(response, 'cookbook/view_category.html')
	 		# Retrieve recipes for that category
	 		recipes = Recipe.objects.filter(category=cat)
	 		content = response.content.decode('utf-8')
	 		# Check recipes are displayed 
	 		for recipe in recipes:
	 			content = response.content.decode('utf-8')
	 			self.assertIn(recipe.name.lower(), content.lower())
	 		
class TestForms(TestCase):

    def setUp(self):
        try:
            from forms import RecipeForm
            from forms import CommentForm

        except ImportError:
            print('The module forms does not exist')
        except NameError:
            print('The class RecipeForm does not exist or is not correct')
        except:
            print('Something else went wrong :-(')
  
    
    def test_add_recipe_form_is_displayed_correctly(self):
        try:
                response = self.client.get(reverse('home'))
                response = self.client.get(reverse('uploadrecipe'))
        except:
            try:
                response = self.client.get(reverse('cookbook:home'))
                response = self.client.get(reverse('cookbook:uploadrecipe'))
            except:
                return False
        # Check form in response context is instance of CategoryForm
        self.assertTrue(isinstance(response.context['form'], PageForm))
        self.assertIn('Name:'.lower(), response.content.lower())

        # Check form is displayed correctly

        # Labels
        self.assertIn('Name:'.lower(), response.content.lower())
        self.assertIn('Picture:'.lower(), response.content.lower())
        self.assertIn('Category:'.lower(), response.content.lower())
        self.assertIn('Ingredients:'.lower(), response.content.lower())
        self.assertIn('Description:'.lower(), response.content.lower())
        self.assertIn('Spice:'.lower(), response.content.lower())
        self.assertIn('Serves:'.lower(), response.content.lower())
        self.assertIn('Cooking time (minutes):'.lower(), response.content.lower())
        self.assertIn('Vegan:'.lower(), response.content.lower())
        self.assertIn('Vegetarian:'.lower(), response.content.lower())
        self.assertIn('Method:'.lower(), response.content.lower())
        self.assertIn('Gluten Free:'.lower(), response.content.lower())
        self.assertIn('Dairy Free:'.lower(), response.content.lower())



def add_user(username, email, password):
    if not User.objects.filter(username=username):
        u = User.objects.get_or_create(username=username, email=email, password=password)[0]
        u.set_password(u.password)
        u.save()
        return u

def add_recipe(username, category, name, picture, description, ingredients,
               method, serves, spice, cooking_time,
               is_vegetarian, is_vegan, is_gluten_free, is_dairy_free):
    
    cat = Category.objects.get(name=category)
        
    r = Recipe.objects.get_or_create(category=cat, name=name,
                                     picture=picture, description=description,
                                     ingredients=ingredients,
                                     method=method, serves=serves,
                                     spice=spice, cooking_time=cooking_time,
                                     is_vegetarian=is_vegetarian,
                                     is_vegan=is_vegan, is_gluten_free=is_gluten_free,
                                     is_dairy_free=is_dairy_free)[0]

    r.save()
    return r



def get_category(self, name):

	from rango.models import Category
	try:
		cat = Category.objects.get(name=name)
	except Category.DoesNotExist:
		cat = None
	return cat

def create_categories():
    # List of categories
    categories = ['Starters','Desserts','Lunches', 'Snacks','Drinks','Mains']


    return categories