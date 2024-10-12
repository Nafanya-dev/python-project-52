from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status


User = get_user_model()


class StatusTestCase(TestCase):
    def setUp(self):
        self.data = {
            'Create_data': {'name': 'new'},
            'Updated_data': {'name': 'completed'},
        }

        self.status = Status.objects.create(name='at work')
        self.user = User.objects.create_user(username='mr_white',
                                             password='123')

        self.urls = {
            'status_list_url': reverse_lazy('status-list-page'),
            'login_url': reverse_lazy('login-page'),
            'create_url': reverse_lazy('create-status-page'),
            'update_url': reverse_lazy('update-status-page',
                                      kwargs={'pk': self.status.pk}),
            'delete_url': reverse_lazy('delete-status-page',
                                      kwargs={'pk': self.status.pk}),
        }

        self.templates = {
            'update_create_form': 'update_create_form.html',
            'delete': 'delete_form.html',
        }
