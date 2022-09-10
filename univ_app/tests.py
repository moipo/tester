from django.test import TestCase

# Create your tests here.
from .models import Test

class TestTestCase(TestCase):

    def setUp(self):
        # self.number_of_tests = 5
        for i in range(5):
            Test.objects.create(title = "Hellow world", description = "something else")

    def test_queryset_exists(self):
        qs = Test.objects.all()
        self.assertEqual(qs.count(), 5)
