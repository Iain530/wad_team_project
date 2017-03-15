from django import forms
from cookbook.models import Category, Recipe, Ingredient, Comment
from django.contrib.auth.models import User

CATEGORIES = (
    ('1', 'starters'),
    ('2', 'dinners'),
    ('3', 'lunches'),
    ('4', 'snacks'),
    ('5', 'desserts'),
    ('6', 'drinks'),
    ) #These need to be Category objects not strings and it should work

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(help_text='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        

class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=Recipe.MAX_NAME_LENGTH,help_text="Recipe Name")
    description=forms.CharField(max_length=Recipe.MAX_DESC_LENGTH,
    						 help_text="Description", widget=forms.Textarea)
    instructions = forms.CharField(max_length=Recipe.MAX_INS_LENGTH, 
    					   help_text="Instructions",widget=forms.Textarea)
    serves = forms.IntegerField(min_value=1, max_value=32767,
                                help_text="Serves")
    cooking_time = forms.IntegerField(min_value=1,
                                      help_text="Cooking time (minutes)")
    
    category = forms.ChoiceField(choices = CATEGORIES, required=True, help_text="Category")
    is_vegetarian = forms.BooleanField(required=False,help_text="Vegetarian" )
    is_vegan = forms.BooleanField(required=False, help_text="Vegan")
    is_gluten_free = forms.BooleanField(required=False, help_text="Gluten Free")
    is_dairy_free = forms.BooleanField(required=False,help_text="Dairy Free")
    
    class Meta:
        model = Recipe
        fields = ('name', 'picture', 'category', 'instructions', 'serves', 'cooking_time',
                  'description', 'is_vegetarian', 'is_vegan', 'is_gluten_free',
                   'is_dairy_free',)
        


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('quantity', 'name',)


class CommentForm(forms.ModelForm):
    text = forms.CharField(required=True, widget=forms.TextInput(attrs={'size':85,}), max_length=Comment.MAX_COMMENT_LENGTH)
    
    class Meta:
        model = Comment
        fields = ('text',)
    
    
