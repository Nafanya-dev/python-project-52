from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from task_manager.labels.models import LabelModel


User = get_user_model()


class LabelTestCase(TestCase):
    def setUp(self):
        self.data = {
            'Create_data': {'name': 'new'},
            'Updated_data': {'name': 'completed'},
        }

        self.label = LabelModel.objects.create(name='at work')
        self.user = User.objects.create_user(username='mr_white',
                                             password='123')

        self.urls = {
            'label_list_url': reverse_lazy('label-list-page'),
            'login_url': reverse_lazy('login-page'),
            'create_url': reverse_lazy('create-label-page'),
            'update_url': reverse_lazy('update-label-page',
                                      kwargs={'pk': self.label.pk}),
            'delete_url': reverse_lazy('delete-label-page',
                                      kwargs={'pk': self.label.pk}),
        }

        self.templates = {
            'update_create_form': 'update_create_form.html',
            'delete': 'delete_form.html',
        }
