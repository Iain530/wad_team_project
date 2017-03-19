from django import forms
from cookbook.models import Category, Recipe, Comment
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(help_text='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

        
class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=Recipe.MAX_NAME_LENGTH,help_text="Recipe Name")
    description=forms.CharField(max_length=Recipe.MAX_DESC_LENGTH,
                                help_text="Description", widget=forms.Textarea(attrs={'rows': 3, 'cols': 60}))
    instructions = forms.CharField(max_length=Recipe.MAX_INS_LENGTH, 
                                   help_text="Instructions",widget=forms.Textarea(attrs={'rows':15, 'cols': 60}))
    serves = forms.IntegerField(min_value=1, max_value=999,
                                help_text="Serves")
    picture = forms.FileField(label='Picture', required = False)
    spice = forms.IntegerField(min_value=0, max_value=5, help_text="Spice")
    cooking_time = forms.IntegerField(min_value=1, max_value=999,
                                      help_text="Cooking time (minutes)",
                                      label="Cooking time (minutes)")
    ingredients = forms.CharField(max_length=Recipe.MAX_INS_LENGTH,
                                  help_text="Ingredients", widget=forms.Textarea(attrs={'rows':15, 'cols': 60}))
    category = forms.ModelChoiceField(queryset= Category.objects.all(), required=True, help_text="Category")
    
    is_vegetarian = forms.BooleanField(required=False,label="Vegetarian" )
    is_vegan = forms.BooleanField(required=False, label="Vegan")
    is_gluten_free = forms.BooleanField(required=False, label="Gluten Free")
    is_dairy_free = forms.BooleanField(required=False, label="Dairy Free")

    SPICE_SET = [(0, 'Not Spicy'),
                 (1, 'Mild'),
                 (2, 'Hot'),
                 (3, 'Super Spicy') ]
    spice = forms.ChoiceField(choices=SPICE_SET, required=True, help_text="Spice")
    
    class Meta:
        model = Recipe
        fields = ('name', 'picture', 'category', 'description', 'ingredients', 'serves', 'cooking_time', 'spice', 'instructions', 
                   'is_vegetarian', 'is_vegan', 'is_gluten_free','is_dairy_free',)
        



class CommentForm(forms.ModelForm):
    text = forms.CharField(required=True, widget=forms.TextInput(attrs={'size':85,}), max_length=Comment.MAX_COMMENT_LENGTH)
    
    class Meta:
        model = Comment
        fields = ('text',)
    
    
