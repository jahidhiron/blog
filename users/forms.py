from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        # way -1
        # fields = UserCreationForm.Meta.fields + ('age', )
        
        # way - 2
        # if we want 
        # fields = ('first_name', 'last_name', 'username', 'email', 'age',)
        fields = ('username', 'email', 'age',)



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        # way -1
        # fields = UserChangeForm.Meta.fields
        
        # way -1
        # if we want 
        # fields = ('first_name', 'last_name', 'username', 'email', 'age',)
        fields = ('username', 'email', 'age',)