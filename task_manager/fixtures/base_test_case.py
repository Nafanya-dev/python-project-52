from django.test import TestCase
from django.contrib.auth import get_user_model

from task_manager.statuses.models import Status


USER = get_user_model()


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = USER.objects.create_user(username='testuser',
                                             password='password')

        self.wrong_user = USER.objects.create_user(username='wronguser',
                                                   password='password')

        self.status = Status.objects.create(name='In Progress')
        self.templates = {
            'update_create_form': 'update_create_form.html',
            'delete': 'delete_form.html'
        }

    def get_urls(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def get_data(self):
        raise NotImplementedError("Subclasses should implement this method.")
