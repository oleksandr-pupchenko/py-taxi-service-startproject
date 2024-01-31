from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Manufacturer, Driver, Car

admin.site.register(Manufacturer)


@admin.register(Driver)
class AdminDrive(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number", )}), )
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number", )}), )


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    search_fields = ["model", "manufacturer"]
