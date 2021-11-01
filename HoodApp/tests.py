from django.test import TestCase
from .models import Neighbourhood
from django.contrib.auth.models import User

# Create your tests here.

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.george = Neighbourhood(neighbourhood='george')

    def test_instane(self):
        self.assertTrue(isinstance(self.george, Neighbourhood))

    def tearDown(self):
        Neighbourhood.objets.all().delete()

    def test_save_method(self):
        self.george.save_neighbourhood()
        thehood = Neighbourhood.objects.all()
        self.assertTrue(len(thehood)>0)
    
    def test_delete_method(self):
        self.george.delete_neighbourhood('george')
        thehood = Neighbourhood.objects.all()
        self.assertTrue(len(thehood)==0)