from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand_name','title','price','is_active') 

@admin.register(FeatureProduct)
class FeatureProductAdmin(admin.ModelAdmin):
    list_display = ('product',)
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','product','is_active',)
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)