from django import forms
from cookbook.models import Category, Recipe, Ingredient, Comment
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        

class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=Recipe.MAX_NAME_LENGTH,
                           help_text="Recipe Name")
    serves = forms.IntegerField(min_value=1, max_value=32767,
                                help_text="Serves")
    cooking_time = forms.IntegerField(min_value=1,
                                      help_text="Cooking time (minutes)")
    
    is_vegetarian = forms.BooleanField(required=False)
    is_vegan = forms.BooleanField(required=False)
    is_gluten_free = forms.BooleanField(required=False)
    is_dairy_free = forms.BooleanField(required=False)

    upload_date = forms.DateTimeField(widget=forms.HiddenInput())

    class Meta:
        model = Recipe
        fields = ('name', 'picture', 'category', 'instructions', 'serves', 'cooking_time',
                   'upload_date', 'is_vegetarian', 'is_vegan', 'is_gluten_free',
                   'is_dairy_free',)


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('quantity', 'name',)


#class CommentForm(forms.ModelForm):
    
    
