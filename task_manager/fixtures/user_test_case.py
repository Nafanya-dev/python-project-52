from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy


User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.data = {
            'Valid_data': {
                "username": "Mr_Blonde+1-@_.",
                "first_name": "Michael",
                "last_name": "Madsen",
                "password1": "Password",
                "password2": "Password",
            },

            'Invalid_data': {
                "username": "Mr_Brown",
                "first_name": "Quentin",
                "last_name": "Tarantino",
                "password1": "Pa",
                "password2": "Pa",
            },

            'User_data': {
                "username": "mr_pink",
                "first_name": "Steve",
                "last_name": "Buscemi",
                "password": "Password",
            },

            'Updated_data': {
                "username": "Mr_Pink",
                "first_name": "Steve",
                "last_name": "Buscemi",
                "password1": "PASSWORD",
                "password2": "PASSWORD",
            }
        }

        self.user = User.objects.create_user(**self.data.get('User_data'))

        self.urls = {
            'user_list_url': reverse_lazy('users-list-page'),
            'create_url': reverse_lazy('register-user-page'),
            'login_url': reverse_lazy('login-page'),
            'update_url': reverse_lazy('update-user-page',
                                       kwargs={'pk': self.user.pk}),
            'delete_url': reverse_lazy('delete-user-page',
                                       kwargs={'pk': self.user.pk}),
        }

        self.templates = {
            'update_create_form': 'update_create_form.html',
            'delete': 'delete_form.html'
        }
