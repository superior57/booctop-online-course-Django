from django.contrib import admin

from django.contrib import admin
from teacher.models import categories, subcategories
from django.contrib.auth import get_user_model
User = get_user_model()


class categoriesList(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'created_at')

class subcategoriesList(admin.ModelAdmin):
    list_display = ('user_categories', 'name', 'image', 'created_at')
admin.site.register(categories, categoriesList)
admin.site.register(subcategories, subcategoriesList)
