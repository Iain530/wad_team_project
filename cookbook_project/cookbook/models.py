from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    # Primary key
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
		
class Recipe(models.Model):
    # Primary key
    name = models.CharField(max_length=128, unique=True)

    # Foreign keys
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
	
    views = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)
    no_of_ratings = models.PositiveIntegerField(default=0)
    upload_date = models.DateTimeField(auto_add_now=True)
	
    # Fields input by user
    ingredients = models.TextField()              # Change field type
    instructions = models.TextField()             # Change field type
    serves = models.PositiveSmallIntegerField()
    cooking_time = models.PositiveIntegerField()
    picture = models.ImageField(upload_to="recipe_images", blank="True")
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_dairy_free = models.BooleanField(default=False)
	
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
	
class Comment(models.Model):
    # Foreign keys
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)
	
    date = models.DateTimeField(auto_add_now=True)
	text = models.CharField(max_length=200)
	
    def __str__(self):
        return self.text	
    def __unicode__(self):
        return self.text