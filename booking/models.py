import uuid
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils.http import urlencode
from django.http import HttpResponse
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import prefetch_related_objects


class Customer(models.Model):

    # Fields
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Metadata
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ("first_name",)

    # Model Functions
    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class Dog(models.Model):
    # Fields
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationships
    owners = models.ManyToManyField(Customer, blank=True, related_name='owners')
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer', null=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    # Relationships
    # appointments = models.ManyToManyField('Appointment', blank=True, related_name='appointments')



    # Metadata
    class Meta:
        verbose_name = 'Dog'
        verbose_name_plural = 'Dogs'
        ordering = ("first_name",)

    # Model Functions
    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class Service(models.Model):
    # Fields
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Metadata
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ("name",)

    # Model Functions
    def __str__(self):
        return str(self.name)


class Appointment(models.Model):
    # Fields
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    email_confirmation = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    # Relationships
    dogs = models.ManyToManyField(Dog, blank=True, related_name='appointment_dogs')
    services = models.ManyToManyField(Service, blank=True)

    # Metadata
    class Meta:
        ordering = ("start_date",)

    # Model Functions
    def __str__(self):
        return str(self.customer.first_name + " " + self.customer.last_name + " " + self.start_date.strftime("%m-%d-%y"))
    

@receiver(post_save, sender=Appointment)
def send_appointment_confirmation(sender, instance, created, **kwargs):
    if created:
        # Process appointment confirmation logic only for newly created appointments
        print_appointment_details(instance)
        print_delivery_confirmation(instance.customer)
        instance.email_confirmation = True
        instance.save()

appointment_created = post_save.connect(send_appointment_confirmation, sender=Appointment)

def print_appointment_details(appointment):
    customer_email = appointment.customer.email
    start_date_formatted = appointment.start_date.strftime("%b %d, %Y")
    end_date_formatted = appointment.end_date.strftime("%b %d, %Y")
    date_range = f"{start_date_formatted} - {end_date_formatted}"
    customer_name = f"{appointment.customer.first_name} {appointment.customer.last_name}"
    dogs = [dog.first_name for dog in appointment.dogs.all()] or "No Dogs Selected"
    services = [service.name for service in appointment.services.all()] or "No Services Selected"
   
    # Format the email details (replace with your desired email format)
    email_body = f"""
    **Appointment Confirmation**

    **Customer Email:** {customer_email}
    **Appointment Date:** {date_range}
    **Customer:** {customer_name}

    **Dogs:**
    {dogs}

    **Services:**
    {services}
    """

    print(email_body)

def print_delivery_confirmation(customer):
    print(f"Email delivery confirmation sent to admin for {customer.first_name} {customer.last_name}'s appointment.")