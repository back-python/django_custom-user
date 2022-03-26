from pyexpat import model
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import CustomUser
from .forms import CustomUserChangedForm, CustomUserCreateForm


@admin.register(CustomUser)
class CustomUserAdmin(auth_admin.UserAdmin):
    model = CustomUser
    form = CustomUserChangedForm
    add_form = CustomUserCreateForm
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ('Campos personalizados', {'fields': ('user_type',)}),
    )
