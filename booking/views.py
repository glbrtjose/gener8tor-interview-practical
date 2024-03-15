from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render

from . import models
from . import forms
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView


# Appointment Views


class AppointmentListView(ListView):
    model = models.Appointment
    template_name = 'booking/appointment_list.html'
    appointments = models.Appointment.objects.all()
    def get(self, request):
        return render(request, self.template_name, {"object_list": self.appointments})

# Code Part 2.1 here
class AppointmentDetailView(DetailView):  # Assuming you already have AppointmentListView
    model = models.Appointment
    template_name = 'booking/appointment_detail.html'  # Adjust template name as needed

class AppointmentCreateView(CreateView):
    model = models.Appointment
    success_url = '/'  # Redirect to homepage after successful creation  # Adjust template name as needed
    fields = ['start_date', 'end_date', 'customer', 'dogs', 'services']
    template_name = 'booking/appointment_form.html'  # Use the provided form template

class AppointmentUpdateView(UpdateView):
    model = models.Appointment
    fields = ['start_date', 'end_date', 'customer', 'dogs', 'services']
    success_url = '/'  # Redirect to homepage after successful update
    template_name = 'booking/appointment_form.html'  # Use the same form template

class AppointmentDeleteView(DeleteView):
    model = models.Appointment
    template_name = 'booking/appointment_confirm_delete.html'  # Confirmation template (optional)
    success_url = '/'