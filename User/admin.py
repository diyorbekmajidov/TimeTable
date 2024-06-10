from django.contrib import admin

# Register your models here.
from .models import (CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Header', {'fields': ['phone_number', 'password',]}),
        ('Personal info', {'fields': ['first_name','last_name']}),
        ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser',]}),
        ('Important dates', {'fields': ['last_login',]}),
    ]

admin.site.register(CustomUser, CustomUserAdmin)