from haystack import indexes
from cookbook.models import Recipe
from django.utils import timezone
import datetime

class RecipeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    category = indexes.CharField(model_attr='category')

    views = indexes.PositiveIntegerField(model_attr='views')
    total_rating = indexes.FloatField(model_attr='total_rating')

    upload_date = indexes.DateTimeField(model_attr='upload_date')
    last_modified = indexes.DateTimeField(model_attr='last_modified')

    serves = indexes.PositiveSmallIntegerField(model_attr='serves')
    cooking_time = indexes.PositiveIntegerField(model_attr='cooking_time')

    is_vegetarian = indexes.BooleanField(model_attr='is_vegetarian')
    is_vegan = indexes.BooleanField(model_attr='is_vegan')
    is_gluten_free = indexes.BooleanField(model_attr='is_gluten_free')
    is_dairy_free = indexes.BooleanField(model_attr='is_dairy_free')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
