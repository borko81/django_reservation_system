from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from owner.views import *


class TestOwnerViews(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_owner_views_not_login(self):
        response = self.client.get(reverse('owner:owner'))
        self.assertEqual(response.status_code, 302)
        
        response = self.client.get(reverse('owner:owner_info'))
        self.assertEqual(response.status_code, 302)
        
        response = self.client.get(reverse('owner:owner_bank'))
        self.assertEqual(response.status_code, 302)
        
        response = self.client.get(reverse('owner:owner_fak_id'))
        self.assertEqual(response.status_code, 302)
       
     
class TestOWnerWithUserLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")
        
    def test_owner_index(self):
        response = self.client.get(reverse('owner:owner'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'owner/base.html')
        
    def test_owner_create_update(self):
        response = self.client.get(reverse('owner:owner_info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'owner/owner_data.html')
        
    def test_owner_bank_view(self):
        response = self.client.get(reverse('owner:owner_bank'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'owner/owner_bank.html')
        
    def test_owner_fak_last_id_views(self):
        response = self.client.get(reverse('owner:owner_fak_id'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'owner/owner_fak_id.html')