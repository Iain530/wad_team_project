from django.contrib import admin
from cookbook.models import Category, Recipe, Comment, Ingredient

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Ingredient)
# Register your models here.
