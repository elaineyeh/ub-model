from django.contrib import admin
from .models import User, Role, Log, State, Link

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Log)
admin.site.register(State)
admin.site.register(Link)
