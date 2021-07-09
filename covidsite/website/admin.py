from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import *

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'name', 'last_login', 'is_admin')
    search_fields = ('email', 'name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    ordering = ('email',)
    # list_filter = ()
    fieldsets = ()
    list_filter = ('is_admin', 'is_active')
    # fieldsets = (
    #     (None, {'fields': ('email', 'password', 'date_joined', 'last_login', )}),
    #     ('Info', {'fields': ('name',)}),
    #     ('Permissions', {'fields': ('is_admin', 'is_applicant' 'is_company')}),
    # )

admin.site.register(User, AccountAdmin)