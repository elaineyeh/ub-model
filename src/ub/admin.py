from django.contrib import admin
from .models import User, ActivityCategory, Log, State, FastLink

# Register your models here.
admin.site.register(User)
admin.site.register(ActivityCategory)
admin.site.register(Log)
admin.site.register(State)
admin.site.register(FastLink)
