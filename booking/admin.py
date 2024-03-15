from django.contrib import admin
from django.utils.html import format_html

# Admin Login
# Username: admin
# Password: admin_password

from .models import Customer, Dog, Service, Appointment
from django import forms

class DogInline(admin.TabularInline):  # Inline for displaying and adding dogs
  model = Dog
  extra = 1  # Show one empty form for adding a new dog initially


class CustomerAdmin(admin.ModelAdmin):
    # Code Part 1.2 here
    list_display = ['id', 'first_name', 'last_name', 'email', 'last_updated', 'created']
    readonly_fields = ['id', 'last_updated', 'created']
    fieldsets = [('Customer Information', {'fields': ['first_name', 'last_name', 'email']}),]
    list_filter = ["last_name"]
    search_fields = ["first_name", "last_name", "email"]
    inlines = [DogInline]  # Include DogInline in the admin form



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Dog)
admin.site.register(Service)
admin.site.register(Appointment)
