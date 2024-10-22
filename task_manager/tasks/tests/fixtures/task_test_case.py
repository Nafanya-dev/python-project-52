from task_manager.tests.base_test_case import BaseTestCase
from django.urls import reverse_lazy
from task_manager.tasks.models import TaskModel


class TaskTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.task = TaskModel.objects.create(
            name='Test Task',
            description='This is a test task.',
            status=self.status,
            author=self.user
        )

    def get_urls(self):
        return {
            'login_url': reverse_lazy('login-page'),
            'task_list_url': reverse_lazy('task-list-page'),
            'create_url': reverse_lazy('create-task-page'),
            'update_url': reverse_lazy('update-task-page',
                                       kwargs={'pk': self.task.pk}),

            'delete_url': reverse_lazy('delete-task-page',
                                       kwargs={'pk': self.task.pk})
        }

    def get_data(self):
        return {
            'Create_data': {
                'name': 'New Task',
                'description': 'Description for new task.',
                'status': self.status.pk,
            },
            'Updated_data': {
                'name': 'Updated Task',
                'description': 'Updated description.',
                'status': self.status.pk,
            },
        }
