from django.urls import resolve, reverse
from django.test import SimpleTestCase

from owner.views import *


class TestOwnerUrls(SimpleTestCase):
    
    def test_view_owner(self):
        url = reverse('owner:owner')
        self.assertEquals(resolve(url).func, owner_index)
        
    def test_create_update_owner_url(self):
        url = reverse('owner:owner_info')
        self.assertEquals(resolve(url).func, owner_create_update)
        
    def test_owner_bank_create_update_url(self):
        url = reverse('owner:owner_bank')
        self.assertEquals(resolve(url).func, owner_bank_create_update)
        
    def test_owner_fak_last_id_url(self):
        url = reverse('owner:owner_fak_id')
        self.assertEquals(resolve(url).func, owner_fak_id_update)