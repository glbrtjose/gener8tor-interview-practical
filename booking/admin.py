from django.contrib import admin
from django.utils.html import format_html

# Admin Login
# Username: admin
# Password: admin_password

from .models import Customer, Dog, Service, Appointment


class CustomerAdmin(admin.ModelAdmin):
    # Code Part 1.2 here
    pass  # Remove this line before you begin


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Dog)
admin.site.register(Service)
admin.site.register(Appointment)
