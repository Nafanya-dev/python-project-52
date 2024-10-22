from task_manager.tests.base_test_case import BaseTestCase
from django.urls import reverse_lazy


class StatusTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

    def get_urls(self):
        return {
            'status_list_url': reverse_lazy('status-list-page'),
            'login_url': reverse_lazy('login-page'),
            'create_url': reverse_lazy('create-status-page'),
            'update_url': reverse_lazy('update-status-page',
                                       kwargs={'pk': self.status.pk}),

            'delete_url': reverse_lazy('delete-status-page',
                                       kwargs={'pk': self.status.pk}),
        }

    def get_data(self):
        return {
            'Create_data': {'name': 'new'},
            'Updated_data': {'name': 'completed'},
        }
