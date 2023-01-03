from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from contragents.models import FirmModel
from contragents.views import *


class ContragentViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_need_user_login(self):
        response = self.client.get(reverse("contragent:menu"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("contragent:contragents"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("contragent:create"))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse("contragent:edit", args=[1]))
        self.assertEqual(response.status_code, 302)


class ContragentViewSuccessUserLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="test", password="test")
        self.client.login(username="test", password="test")
        FirmModel.objects.create(name=1)

    def test_url_user_login(self):
        response = self.client.get(reverse("contragent:menu"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contragents/base.html")

        response = self.client.get(reverse("contragent:contragents"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contragents/show_all.html")

        response = self.client.get(reverse("contragent:create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contragents/create.html")

        response = self.client.get(reverse("contragent:edit", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contragents/create.html")
