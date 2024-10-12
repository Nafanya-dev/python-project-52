from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from task_manager.tasks.models import TaskModel


User = get_user_model()


class TaskTestCase(TestCase):
    def setUp(self):
        self.status = Status.objects.create(name='In Progress')
        self.user = User.objects.create_user(username='testuser', password='password')
        self.wrong_user = User.objects.create_user(username='wronguser', password='password')
        self.task = TaskModel.objects.create(
            title='Test Task',
            description='This is a test task.',
            status=self.status,
            author=self.user
        )

        self.data = {
            'Create_data': {
                'title': 'New Task',
                'description': 'Description for new task.',
                'status': self.status.pk,
            },
            'Updated_data': {
                'title': 'Updated Task',
                'description': 'Updated description.',
                'status': self.status.pk,
            },
        }

        self.urls = {
            'login_url': reverse_lazy('login-page'),
            'task_list_url': reverse_lazy('task-list-page'),
            'create_url': reverse_lazy('create-task-page'),
            'update_url': reverse_lazy('update-task-page', kwargs={'pk': self.task.pk}),
            'delete_url': reverse_lazy('delete-task-page', kwargs={'pk': self.task.pk})
        }

        self.templates = {
            'update_create_form': 'update_create_form.html',
            'delete': 'delete_form.html'
        }
