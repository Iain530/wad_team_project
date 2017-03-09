from django.contrib import admin
from cookbook.models import Category, Recipe, Comment, Ingredient, Rating

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Ingredient)
admin.site.register(Rating)
# Register your models here.
