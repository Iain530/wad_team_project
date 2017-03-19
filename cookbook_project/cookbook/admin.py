from django.contrib import admin
from cookbook.models import Category, Recipe, Comment, Rating

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Rating)
# Register your models here.
