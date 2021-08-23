from core.admin import admin_site
from django.contrib import admin
from .models import ContactList, ContactNameList, User, Role, Log, State, Link, Contact, Activity, UserActivity


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


class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'activity_name',
        'unit_name',
        'apply_qualification_list',
        'apply_start_date',
        'apply_end_date',
        'post_start_time',
        'post_end_time'
    )


class UserActivityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fb_id',
        'activity'
    )


class ContactListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )


class ContactNameListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )


admin_site.register(User, UserAdmin)
admin_site.register(Role, RoleAdmin)
admin_site.register(Log, LogAdmin)
admin_site.register(State, StateAdmin)
admin_site.register(Link, LinkAdmin)
admin_site.register(Contact, ContactAdmin)
admin_site.register(Activity, ActivityAdmin)
admin_site.register(UserActivity, UserActivityAdmin)
admin_site.register(ContactList, ContactListAdmin)
admin_site.register(ContactNameList, ContactNameListAdmin)
