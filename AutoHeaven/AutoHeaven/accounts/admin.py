

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from AutoHeaven.accounts.models import AppAccount, Profile


# Register your models here.
@admin.register(AppAccount)
class AppAccountAdmin(UserAdmin):
    # Fields to display in the admin list view
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')  # Enable search for username and email
    list_filter = ('is_staff', 'is_active')  # Filter by staff status and active status
    ordering = ('username',)  # Default order by username

    # Fieldsets for viewing and editing
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    # Fields required when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('user', 'first_name', 'last_name', 'age', 'height')
    search_fields = ('user__username', 'first_name', 'last_name')  # Enable search for user, first and last name
    list_filter = ('age',)  # Add filters for age
    ordering = ('user__username',)  # Default order by user's username

    # Fields to display in the detailed view
    fieldsets = (
        (None, {'fields': ('user', 'first_name', 'last_name', 'age', 'height')}),
    )