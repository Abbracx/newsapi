from django.contrib import admin
from .models import Article, Journalist

# Register your models here.

@admin.register(Article)
class Article(admin.ModelAdmin):
    pass

@admin.register(Journalist)
class Journalist(admin.ModelAdmin):
    pass
