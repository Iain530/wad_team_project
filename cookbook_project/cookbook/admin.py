from django.contrib import admin
from cookbook.models import Category, Recipe, Comment

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Comment)
# Register your models here.
