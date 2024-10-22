from task_manager.tests.base_test_case import BaseTestCase
from django.urls import reverse_lazy
from task_manager.labels.models import LabelModel


class LabelTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.label = LabelModel.objects.create(name='at work')

    def get_urls(self):
        return {
            'label_list_url': reverse_lazy('label-list-page'),
            'login_url': reverse_lazy('login-page'),
            'create_url': reverse_lazy('create-label-page'),
            'update_url': reverse_lazy('update-label-page',
                                       kwargs={'pk': self.label.pk}),

            'delete_url': reverse_lazy('delete-label-page',
                                       kwargs={'pk': self.label.pk}),
        }

    def get_data(self):
        return {
            'Create_data': {'name': 'new'},
            'Updated_data': {'name': 'completed'},
        }
