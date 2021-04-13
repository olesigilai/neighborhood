from django.test import TestCase
from django.contrib.auth.models import User
from .models import healthservices,neighbourhood

import datetime as dt
# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.kataret = neighbourhood(neighbourhood='kataret')

    def test_instance(self):
        self.assertTrue(isinstance(self.kataret,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.kataret.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

