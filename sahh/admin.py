from django.contrib import admin

from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    """
    docstring
    """
    pass

admin.site.register(CustomUser,UserModel)