from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from FitnessStats.accounts.models import AppAccount, Profile


# Register your models here.
@admin.register(AppAccount)
class AppAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass