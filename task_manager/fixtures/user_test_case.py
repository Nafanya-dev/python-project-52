from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy


User = get_user_model()


class UserRegisterTestCase(TestCase):
    def setUp(self):
        self.url = reverse_lazy('register-user-page')

        self.valid_data = {
            "username": "Mr_Blonde+1-@_.",
            "first_name": "Michael",
            "last_name": "Madsen",
            "password1": "Password",
            "password2": "Password"
        }

        self.invalid_data = {
            "username": "Mr_Brown",
            "first_name": "Quentin",
            "last_name": "Tarantino",
            "password1": "Pa",
            "password2": "Pa"
        }


class UserUpdateDeleteTestCase(TestCase):
    def setUp(self):
        self.create_data = {
            "username": "mr_pink",
            "first_name": "Steve",
            "last_name": "Buscemi",
            "password1": "Password",
            "password2": "Password"
        }

        self.updated_data = {
            "username": "Mr_Pink",
            "first_name": "Steve",
            "last_name": "Buscemi",
            "password1": "PASSWORD",
            "password2": "PASSWORD"
        }

        self.user = User.objects.create_user(self.create_data)

        self.update_url = reverse_lazy('update-user-page',
                                       kwargs={'pk': self.user.pk})
        # Замените на ваш URL
        self.delete_url = reverse_lazy('delete-user-page',
                                       kwargs={'pk': self.user.pk})
