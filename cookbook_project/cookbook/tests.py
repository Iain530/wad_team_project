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

class ViewTests(TestCase):
    def test_index_context(self):
        # Access index with empty database
        response = self.client.get(reverse('cookbook:home'))

        # Context dictionary is then empty
        self.assertItemsEqual(response.context['categories'], [])
        self.assertItemsEqual(response.context['recipes'], [])

        categories = test_utils.create_categories()
        test_utils.create_pages(categories)

        #Access index with database filled
        response = self.client.get(reverse('cookbook:home'))

        #Retrieve categories and recipes from database
        pages = Page.objects.order_by('-upload_date')

        # Check context dictionary filled
        self.assertItemsEqual(response.context['categories'], categories)
        self.assertItemsEqual(response.context['pages'], pages)
        


def test_starters_displays_no_recipes_message(self):
	# Access index with empty database
	response = self.client.get(reverse('cookbook:starters'))
	# Check if no categories message is displayed
	self.assertIn("There are no recipes present.", response.content)
	
def test_mains_displays_no_recipes_message(self):
	# Access index with empty database
	response = self.client.get(reverse('cookbook:mains'))
	# Check if no categories message is displayed
	self.assertIn("There are no recipes present.", response.content)

def test_lunches_displays_no_recipes_message(self):    
	# Access index with empty database
	response = self.client.get(reverse('cookbook:lunches'))
	# Check if no categories message is displayed
	self.assertIn("There are no recipes present.", response.content)
	
def test_desserts_displays_no_recipes_message(self):
	# Access index with empty database
	response = self.client.get(reverse('cookbook: desserts'))
	# Check if no categories message is displayed
	self.assertIn("There are no recipes present.", response.content)

def test_snacks_displays_no_recipes_message(self):
	# Access index with empty database
	response = self.client.get(reverse('cookbook: snacks'))
	# Check if no categories message is displayed
	self.assertIn("There are no recipes present.", response.content)

def test_drinks_displays_no_recipes_message(self):
	# Access index with empty database
	response = self.client.get(reverse('cookbook: drinks'))
	# Check if no categories message is displayed
	self.assertIn("There are no recipes present.", response.content)
	
# For each category check the context dictionary passed via render() function
def test_category_context(self):
	for category in categories:
		response = self.client.get(reverse('show_category', args=[category.slug]))
		pages = Page.objects.filter(category=category)
		self.assertItemsEqual(response.context['recipes'], recipes)
		self.assertEquals(response.context['category'], category)



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

class CategoryPageTests(TestCase):
	
	def test_categories_using_template(self):
		# Check the template used to render categories page
		response = self.client.get(reverse('cookbook:categories'))
		self.assertTemplateUsed(response, 'cookbook/categories.html')
	
	def test_index_has_title(self):
		# Check it has title
		response = self.client.get(reverse('cookbook:categories'))
		self.assertIn('Categories'.lower(), response.content.lower())
	
	def test_does_categories_contain_img(self):
		# Check if the categories page contains an img
		response = self.client.get(reverse('cookbook:categories'))
		self.assertIn('img', response.content)

def test_category_page_displays_pages(self):
	# For each category, access its page and check for the pages associated with it
	for category in categories:
		# Access category page
		response = self.client.get(reverse('show_category', args=[category.slug]))
		# Retrieve pages for that category
		pages = Page.objects.filter(category=category)
		# Check pages are displayed and they have a link
		for page in pages:
			self.assertIn(page.title, response.content)
			self.assertIn(page.url, response.content)
		

class ModelTests(TestCase):

    def setUp(self):
        try:
            from populate_cookbook import populate
            populate()
        except ImportError:
            print('The module populate_cookbook does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

def get_category(self, name):
	from rango.models import Category
	try:
		cat = Category.objects.get(name=name)
	except Category.DoesNotExist:
		cat = None
	return cat

# check admin interface - is it configured and set up
def test_admin_interface_page_view(self):
    from admin import PageAdmin
    self.assertIn('category', PageAdmin.list_display)
    self.assertIn('url', PageAdmin.list_display)

def test_does_slug_field_work(self):
    from rango.models import Recipe
    recipe = Recipe(name='how do i create a slug in django')
    recipe.save()
    self.assertEqual(recipe.slug,'how-do-i-create-a-slug-in-django')

class ViewTests(TestCase):

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

    pass    

def test_create_pages(self):
	cat = Category(name="Starters")
	cat.save()
	
	recipe1 = Recipe()
	recipe1.category = cat
	recipe1.name = "Steak pie"
	recipe1.description = "A lovely family friendly steak pie"
	recipe1.picture = os.path.join('recipe_images', 'HummusLover123', 'tofu-curry.jpg')
	recipe1.ingredients = "A pie"
	recipe1.serves = 4
	recipe1.spice = 1
	recipe1.cooking_time = 60
	recipe1.is_vegetarian = False
	recipe1.is_vegan = False
	recipe1.is_gluten_free = False
	recipe1.is_dairy_free = False
	recipe1.save()
	
	starters_recipes = cat.page_set.all()
	self.assertEquals(starters_recipe.count(), 1)
	
	first_recipe = starters_recipes[0]
	self.assertEquals(first_page, recipe1)
	self.assertEquals(first_page.name, "Steak pie")
	self.assertEquals(first_page.serves, 3)

