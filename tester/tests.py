from django.test import TestCase
from django.conf import settings #отсюда тоже можно взять
#всё что есть в модуле settings.
from django.contrib.auth.password_validation import validate_password
import os

#unittest
class TryDjangoConfigTest(TestCase):
    def test_anyname(self):
        self.assertTrue(1==1)
        self.assertEqual(1,2)

    def test_secret_key_strangth(self):
        SECRET_KEY = os.environ.get("SECRET_KEY")
        try:
            pass #dosomething
        except Exception as e:
            self.fail(e)
