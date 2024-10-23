from task_manager.tests.base_test_case import BaseTestCase
from django.urls import reverse_lazy


class UserTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

    def get_urls(self):
        return {
            'user_list_url': reverse_lazy('user-list-page'),
            'create_url': reverse_lazy('register-user-page'),
            'login_url': reverse_lazy('login-page'),
            'update_url': reverse_lazy('update-user-page',
                                       kwargs={'pk': self.user.pk}),
            'delete_url': reverse_lazy('delete-user-page',
                                       kwargs={'pk': self.user.pk}),
        }

    def get_data(self):
        return {
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

            'Updated_data': {
                "username": "Mr_Pink",
                "first_name": "Steve",
                "last_name": "Buscemi",
                "password1": "PASSWORD",
                "password2": "PASSWORD",
            }
        }
