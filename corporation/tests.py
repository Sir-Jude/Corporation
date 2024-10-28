from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Corporation


User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user",
            password="test_pass",
            name="John Doe",
        )
    
    def test_user_creation(self):
        assert self.user.username == "test_user"
        assert not self.user.username == "wrong_user"
        assert self.user.check_password("test_pass")
        assert not self.user.check_password("wrong_pass")
        assert self.user.name == "John Doe"
        assert not self.user.name == "Wrong Name"

    def test_get_absolute_url(self):
        expected_url = "/users/test_user/"
        wrong_url = "/users/wrong_url"
        assert self.user.get_absolute_url() == expected_url
        assert not self.user.get_absolute_url() == wrong_url


class CorporationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user",
            password="test_pass",
            name="John Doe",
        )
        
        self.corporation = Corporation.objects.create(
            user=self.user,
            corporation_name="Test Corporation",
            sector="Technology",
            address="Berlinerstrasse 69, 12345, Berlin",
            phone_number="0123 45 67 89",
            email="info@corporation.com",
        )
    
    def test_corporation_creation(self):
        assert self.corporation.user.username == "test_user"
        assert not self.corporation.user.username == "wrong_user"
        assert self.corporation.corporation_name == "Test Corporation"
        assert not self.corporation.corporation_name == "Wrong Corporation"
        assert self.corporation.sector == "Technology"
        assert not self.corporation.sector == "Farming"
        assert self.corporation.phone_number == "0123 45 67 89"
        assert not self.corporation.phone_number == "0897 65 43 21"
        assert self.corporation.email == "info@corporation.com"
        assert not self.corporation.email == "wrong@corporation.com"
    
    def test_corporation_str(self):
        assert str(self.corporation) == "Test Corporation"
        assert not str(self.corporation) == "Wrong Corporation"