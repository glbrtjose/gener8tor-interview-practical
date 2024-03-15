from django.test import TestCase
from .models import *
from datetime import datetime    


######################  Customer Model Tests ######################


class CustomerTest(TestCase):
    
    def setUp(self):
       # Code Part 3.1 here
        self.customer_data = {
            'first_name': 'Gilberto',
            'last_name': 'Parra',
            'email': 'gilbertocarrizo@gmail.com',
        }
        Customer.objects.create(**self.customer_data)

    def tearDown(self):
        # Code Part 3.1 here
        Customer.objects.all().delete()

    def test_create(self):
        # Code Part 3.1 here
        self.customer_data = {
            'first_name': 'Gilberto',
            'last_name': 'Parra',
            'email': 'gilbertocarrizo@gmail.com',
        }
        Customer.objects.create(**self.customer_data)

    def test_read(self):
        # Code Part 3.1 here
        Customer.objects.all()
        
    def test_update(self):
        # Code Part 3.1 here
        self.customer_data = {
            'first_name': 'Gilberto',
            'last_name': 'Parra2',
            'email': 'gilbertocarrizo@gmail.com',
        }
        Customer.objects.all().filter(first_name='Gilberto').update(**self.customer_data)

    def test_delete(self):
        # Code Part 3.1 here
        Customer.objects.all().filter(first_name='Gilberto').delete()


######################  Dog Model Tests ######################


class DogTest(TestCase):
    # Code Part 3.1 here    
    def setUp(self):
       # Code Part 3.1 here
        self.dog_data = {
            'first_name': 'Spike',
            'last_name': 'Pickles',
        }
        Dog.objects.create(**self.dog_data)

    def tearDown(self):
        # Code Part 3.1 here
        Dog.objects.all().delete()

    def test_create(self):
        # Code Part 3.1 here
        self.dog_data = {
            'first_name': 'Spike',
            'last_name': 'Pickles',
        }
        Dog.objects.create(**self.dog_data)

    def test_read(self):
        # Code Part 3.1 here
        Dog.objects.all()
        
    def test_update(self):
        # Code Part 3.1 here
        self.dog_data = {
            'first_name': 'Spike',
            'last_name': 'Pickles2',
        }
        Dog.objects.all().filter(first_name='Spike').update(**self.dog_data)

    def test_delete(self):
        # Code Part 3.1 here
        Dog.objects.all().filter(first_name='Spike').delete()


######################  Service Model Tests ######################


class ServiceTest(TestCase):
    # Code Part 3.1 here
    def setUp(self):
       # Code Part 3.1 here
        self.dog_data = {
            'name': 'Shower',
            'description': 'Dog shower',
        }
        Service.objects.create(**self.dog_data)

    def tearDown(self):
        # Code Part 3.1 here
        Service.objects.all().delete()

    def test_create(self):
        # Code Part 3.1 here
        self.dog_data = {
            'name': 'Shower',
            'description': 'Dog shower',
        }
        Service.objects.create(**self.dog_data)

    def test_read(self):
        # Code Part 3.1 here
        Service.objects.all()
        
    def test_update(self):
        # Code Part 3.1 here
        self.dog_data = {
            'name': 'Shower',
            'description': 'Dog shower',
        }
        Service.objects.all().filter(name='Shower').update(**self.dog_data)

    def test_delete(self):
        # Code Part 3.1 here
        Service.objects.all().filter(name='Shower').delete()


######################  Appointment Model Tests ######################


class AppointmentTest(TestCase):
    # Code Part 3.1 here
    def setUp(self):
       # Code Part 3.1 here
        self.customer_data = {
            'first_name': 'Gilberto',
            'last_name': 'Parra',
            'email': 'gilbertocarrizo@gmail.com',
        }
        customer = Customer.objects.create(**self.customer_data)
        self.appointment_data = {
            'start_date': datetime.now(),
            'end_date': datetime.now(),
            'email_confirmation': False,
            'customer': customer
        }
        Appointment.objects.create(**self.appointment_data)

    def tearDown(self):
        # Code Part 3.1 here
        Appointment.objects.all().delete()

    def test_create(self):
        # Code Part 3.1 here
        customer = Customer.objects.first()
        self.appointment_data = {
            'start_date': datetime.now(),
            'end_date': datetime.now(),
            'email_confirmation': False,
            'customer': customer
        }
        Appointment.objects.create(**self.appointment_data)

    def test_read(self):
        # Code Part 3.1 here
        Appointment.objects.all()
        
    def test_update(self):
        # Code Part 3.1 here
        customer = Customer.objects.first()
        today = datetime.now()
        self.appointment_data = {
            'start_date': today,
            'end_date': today,
            'email_confirmation': False,
            'customer': customer
        }
        Appointment.objects.all().filter(start_date=today).update(**self.appointment_data)

    def test_delete(self):
        # Code Part 3.1 here
        today = datetime.now()
        Appointment.objects.all().filter(start_date=today).delete()