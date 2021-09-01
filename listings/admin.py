from django.contrib import admin
from .models import Category,Product,Review,Return

class OrderReviewInline(admin.TabularInline):
    model = Review
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','slug')
    prepopulated_fields={'slug':('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','slug','price','available')
    list_filter=('category','available')
    prepopulated_fields={'slug':('name',)}
    inlines=[OrderReviewInline]
@admin.register(Return)
class ReturnAdmin(admin.ModelAdmin):
    list_display=('product_name','email','phone',"date_and_time_of_purchasing")
    list_filter=('date_and_time_of_purchasing','phone')


