from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class HomePageTestCase(SimpleTestCase):

    def test_home_page(self):
        response  = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignupTestCase(TestCase):

    username = 'newuser'
    email = 'newuser@gmail.com'

    def test_signup_page(self):

        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )

        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
