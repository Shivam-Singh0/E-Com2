
from django.contrib import admin
from .models import  Account
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q
from django.db import models

from django.contrib.auth.backends import ModelBackend
# Register your models here.

class AcountAdmin(UserAdmin):
    list_display = ('email','first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('date_joined',)
    filter_horizontal =()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AcountAdmin)





