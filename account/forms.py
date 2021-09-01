from django import  forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Custom
class CustomCreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Custom
   
        fields=UserCreationForm.Meta.fields + ('age','phone','email') 
        
class CustomChange(UserChangeForm):
    class Meta:
        model=Custom
        fields=UserChangeForm.Meta.fields
