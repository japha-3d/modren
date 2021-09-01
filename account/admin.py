from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin
from .forms import CustomCreation,CustomChange
from .models import Custom

class CustomAdmin(UserAdmin):
    add_form=CustomCreation
    form=CustomChange
    model=Custom
    list_display=['username','age','is_staff','email','phone']
admin.site.register(Custom,CustomAdmin)
