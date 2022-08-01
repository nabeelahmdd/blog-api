from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from myapp.models import *

# Register your models here.

# Author register to admin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile',)
    search_fields = ('name',)
    list_filter = ('created_at',)

admin.site.register(Author, AuthorAdmin)

# Category register to admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)

admin.site.register(Category, CategoryAdmin)


# Article register to admin
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', )
    search_fields = ('title',)
    list_filter = ('cr_date',)

admin.site.register(Article, ArticleAdmin)