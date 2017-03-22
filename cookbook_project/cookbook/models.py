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
	
    class Meta:
        verbose_name_plural = 'Categories'	

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
    try:
        image = Image.open(picture)

        if image.size != (side, side):
            (width, height) = image.size
            scale = min(width, height)/ (side*1.0)
            size = ( int(width/scale), int(height/scale) )
            image = image.resize(size, Image.ANTIALIAS)
            trim = ( side, side )
            image = ImageOps.fit(image, trim, Image.ANTIALIAS)
            image.save(picture.path)
    except:
        pass

# file name for recipe images
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
    weighted_rating = models.FloatField(default=0)
    
    upload_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(null=True)

	
    # Fields input by user
    MAX_NAME_LENGTH = 25
    MAX_DESC_LENGTH = 65
    MAX_INS_LENGTH = 32767
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    slug = models.SlugField() # name as slug
    description = models.CharField(max_length=MAX_DESC_LENGTH)
    method = models.TextField(blank=True)             # Change field type
    ingredients = models.TextField(default="")
    spice = models.IntegerField(default=0)
    serves = models.PositiveSmallIntegerField()
    cooking_time = models.PositiveIntegerField(default=0)
    picture = models.ImageField(upload_to=recipe_file_name, blank=True)
    
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
        if 0 <= rate <= 5 and user != self.user:
            rating = Rating.objects.filter(recipe=self, user=user)
            if len(rating) > 0:
                rating = rating[0]
                rating.value = rate
            
            else:
                rating = Rating.objects.create(recipe=self, user=user, value=rate)
            rating.save()

            # calculate rating
            all_ratings = Rating.objects.filter(recipe=self)
            self.no_of_ratings = len(all_ratings)
            if self.no_of_ratings > 0:
                tot = 0.0
                # find total
                for r in all_ratings:
                    tot += r.value
                # use total to get average rating
                self.total_rating = tot / self.no_of_ratings

                # WEIGHTED RATING USED FOR BEST RATED
                # Weighted rating will be > 0 if total rating is > 3.5
                # and number of ratings is > 3. (can be increased when
                # database size increases)

                # minimum rating to be included in best rated (between 0 and 5)
                min_r = 3.5
                # minimum number of ratings needed to be included in best rated
                min_no = 3
                
                if self.total_rating > min_r and self.no_of_ratings >= min_no:
                    self.weighted_rating = ((self.total_rating - min_r + 1)**2)*(self.no_of_ratings - min_no + 1)
                else:
                    self.weighted_rating = 0
                
            self.save()
            return rating.value
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
	
class Comment(models.Model):
    MAX_COMMENT_LENGTH = 512
    
    # Foreign keys
    user = models.ForeignKey(User)
    recipe = models.ForeignKey(Recipe)
	
    upload_date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=MAX_COMMENT_LENGTH)
	
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

    
