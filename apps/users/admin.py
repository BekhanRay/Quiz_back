from django.contrib import admin
from django.contrib.auth import admin as a, models

from apps.users.management.forms import UserCreationForm, UserChangeForm
from .models import User


@admin.register(User)
class UserAdmin(a.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ('username', 'is_staff',)
    list_filter = ('is_staff',)

    fieldsets = (
        (None, {'fields': ('username', 'password', 'is_staff', 'user_permissions')}),
    )

    add_fieldsets = (
        "New user", {"classes": ("wide",),
                     "fields": (
                         "username",
                         "password1",
                         "password2",
                         "is_staff",
                         "user_permissions")}),

    verbose_name = 'User'
    verbose_name_plural = 'Users'


admin.site.unregister(models.Group)
