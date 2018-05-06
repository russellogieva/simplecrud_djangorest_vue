from django.contrib import admin

# Register your models here.
from .models import Role, Users

admin.site.register(Role)
admin.site.register(Users)