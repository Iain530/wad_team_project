from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from PIL import Image, ImageOps
import os
import datetime

class Category(models.Model):
    # Primary key
    name = models.CharField(max_length=128, primary_key=True)
    picture = models.ImageField(upload_to="category_images", blank=True)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):   
        super(Category, self).save(*args, **kwargs)

        # resize recipe picture
        if self.picture:
            resizePicture(self.picture, 250)

# resizes a picture to a square of with sides of length (size)px 
def resizePicture(picture, side):
    image = Image.open(picture)

    if image.size != (side, side):
        (width, height) = image.size
        scale = min(width, height)/ (side*1.0)
        size = ( int(width/scale), int(height/scale) )
        image = image.resize(size, Image.ANTIALIAS)
        trim = ( side, side )
        image = ImageOps.fit(image, trim, Image.ANTIALIAS)
        image.save(picture.path)

def recipe_file_name(instance, filename):
    return os.path.join('recipe_images', instance.user.username, filename)
    
		
class Recipe(models.Model):
    # Foreign keys
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)

    # Users that save this recipe
    saved_by = models.ManyToManyField(User, related_name='saved_recipes', blank=True)
    
    views = models.PositiveIntegerField(default=0)
    total_rating = models.FloatField(default=0)
    no_of_ratings = models.PositiveIntegerField(default=0)
    
    upload_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(default=timezone.now)

	
    # Fields input by user
    MAX_NAME_LENGTH = 128
    MAX_DESC_LENGTH = 400
    MAX_INS_LENGTH = 2000
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    slug = models.SlugField() # name as slug
    description = models.CharField(max_length=MAX_DESC_LENGTH)
    instructions = models.TextField()             # Change field type
    serves = models.PositiveSmallIntegerField()
    cooking_time = models.PositiveIntegerField(default=0)
    picture = models.ImageField(upload_to=recipe_file_name, blank="True")
    
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_dairy_free = models.BooleanField(default=False)
	
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

    # not sure if this works
    def rate(self, user, rate):
        if 0 <= rate <= 5:
            new_rating = Rating.objects.get_or_create(recipe=self, user=user)[0]
            new_rating.value = rate
            new_rating.save()

            # calculate rating
            all_ratings = Rating.objects.filter(recipe=self)
            self.no_of_ratings = len(all_ratings)
            if self.no_of_ratings > 0:
                tot = 0.0
                for r in all_ratings:
                    tot += r.value
                self.total_rating = tot / self.no_of_ratings

                # TODO weighted rating here
            self.save()
            return (self.no_of_ratings)
        else:
            print('Invalid rating: {0}'.format(rate))
            return None

    def user_save(self, user):
        self.saved_by.add(user)
        self.save()

    def user_unsave(self, user):
        self.saved_by.remove(user)
        self.save()

    def save(self, *args, **kwargs):
        # get slug
        self.slug = slugify(self.name)

        # vegan <=> vegetarian and dairy free
        if self.is_vegan or (self.is_vegetarian and self.is_dairy_free):
            self.is_vegan = True
            self.is_vegetarian = True
            self.is_dairy_free = True
        
        super(Recipe, self).save(*args, **kwargs)

        # resize recipe picture
        if self.picture:
            resizePicture(self.picture, 200)

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


class Rating(models.Model):
    # Foreign Keys
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)

    value = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.value	
    def __unicode__(self):
        return self.value

    
