from core.admin import admin_site
from django.contrib import admin
from .models import User, Role, Log, State, Link, Contact

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'fb_id',
        'state',
        'subscribed',
        'role'
    )


class RoleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class LogAdmin(admin.ModelAdmin):
    list_display = (
        'log',
    )


class StateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'label',
        'parent',
        'function',
        'is_input'
    )


class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'button_label'
    )


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fb_id',
        'contact'
    )

admin_site.register(User, UserAdmin)
admin_site.register(Role, RoleAdmin)
admin_site.register(Log, LogAdmin)
admin_site.register(State, StateAdmin)
admin_site.register(Link, LinkAdmin)
admin_site.register(Contact, ContactAdmin)
