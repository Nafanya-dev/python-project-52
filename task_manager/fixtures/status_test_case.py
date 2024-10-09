from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status


User = get_user_model()


class StatusTestCase(TestCase):
    def setUp(self):
        self.update_data = {'name': 'completed'}
        self.create_data = {'name': 'new'}

        self.status_list_url = reverse_lazy('status-list-page')
        self.login_url = reverse_lazy('login-page')
        self.create_url = reverse_lazy('create-status-page')

        self.update_create_template = 'statuses/update_create_status_form.html'
        self.delete_template = 'statuses/delete_status.html'

        self.user = User.objects.create_user(username='mr_white',
                                             password='123')

        self.status = Status.objects.create(name='at work')

        self.update_url = reverse_lazy('update-status-page',
                                       kwargs={'pk': self.status.pk})

        self.delete_url = reverse_lazy('delete-status-page',
                                       kwargs={'pk': self.status.pk})
