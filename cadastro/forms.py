from django.contrib.auth import forms
from .models import CustomUser


class CustomUserChangedForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):    
        model = CustomUser


class CustomUserCreateForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = CustomUser
