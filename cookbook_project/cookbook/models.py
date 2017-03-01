from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

class Category(models.Model):
    # Primary key
    name = models.CharField(max_length=128, primary_key=True)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
		
class Recipe(models.Model):
    # Foreign keys
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)

    # Users that save this recipe
    saved_by = models.ManyToManyField(User, related_name='saved_recipes', blank=True)
    rated_by
    
    views = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
    no_of_ratings = models.PositiveIntegerField(default=0)
    
    upload_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(default=timezone.now)

	
    # Fields input by user
    MAX_NAME_LENGTH = 128
    MAX_DESC_LENGTH = 400
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    slug = models.SlugField() # name as slug
    description = models.CharField(max_length=MAX_DESC_LENGTH)
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

    # not sure if this works
    def rate(self, rate):
        if 0 <= rate <= 5:
            new_rating = self.rating * self.no_of_ratings
            new_rating += rate
            self.no_of_ratings += 1
            new_rating = new_rating / self.no_of_ratings
            self.rating = new_rating
            self.save()
        else:
            print('Invalid rating: {0}'.format(rate))

    def user_save(self, user):
        self.saved_by.add(user)
        self.save()

    def user_unsave(self, user):
        self.saved_by.remove(user)
        self.save()

    def save(self, *args, **kwargs):
        # get slug
        self.slug = slugify(self.name)

        # get rating
        #self.no_of_ratings = len(Rating.objects.filter(recipe=self))
        #if self.no_of_ratings > 0:
            
        
        super(Recipe, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('user', 'slug')

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    name = models.CharField(max_length=64)
    quantity = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
	
class Comment(models.Model):
    # Foreign keys
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)
	
    upload_date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)
	
    def __str__(self):
        return self.text	
    def __unicode__(self):
        return self.text


##class Rating(models.Model):
##    # Foreign Keys
##    user = models.ForeignKey(User)
##    recipe = models.ForeignKey(Recipe)
##
##    value = models.PositiveSmallIntegerField()
##
##    def __str__(self):
##        return self.value	
##    def __unicode__(self):
##        return self.value

    
