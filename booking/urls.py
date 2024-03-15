from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppointmentListView.as_view(), name='book_appointment'),
    # Code Part 2.2 here
    path('book_appointment/', views.AppointmentCreateView.as_view(), name='appointment_form'),
    path('appointment_details/<uuid:pk>/', views.AppointmentDetailView.as_view(), name='appointment_details'),
    path('edit_appointment/<uuid:pk>/', views.AppointmentUpdateView.as_view(), name='edit_appointment'),
    path('delete_appointment/<uuid:pk>/', views.AppointmentDeleteView.as_view(), name='delete_appointment'),
]
